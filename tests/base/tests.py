import os
import unittest

import troposphere

from gordon.resources.base import BaseStream
from gordon.utils import load_settings
from gordon.utils_tests import BaseIntegrationTest, BaseBuildTest

try:
    from mock import patch, Mock
except ImportError:
    from unittest.mock import patch, Mock


class IntegrationTest(BaseIntegrationTest):

    def test_0001_project(self):
        self._test_project_step('0001_project')
        self.assert_stack_succeed('p')
        self.assert_stack_succeed('r')


class BuildTest(BaseBuildTest):

    def test_0001_project(self):
        self._test_project_step('0001_project')
        self.assertBuild('0001_project', '0001_p.json')
        self.assertBuild('0001_project', '0002_pr_r.json')
        self.assertBuild('0001_project', '0003_r.json')


class BatchSizeTest(unittest.TestCase):

    def test_batch_size_read_from_settings(self):
        settings = {
            'lambda': '',
            'stream': '',
            'starting_position': '',
            'batch_size': troposphere.Ref('BatchSize')
        }
        app = Mock(name='app')
        app.name = 'app'
        stream = BaseStream(
            name='dummy', settings=settings, app=app, project=Mock()
        )

        self.assertEqual(stream.get_batch_size(), 123)

    # def test_batch_size_minimum_respected(self):
    #     raise NotImplementedError
    #
    # def test_batch_size_maximum_respected(self):
    #     raise NotImplementedError
