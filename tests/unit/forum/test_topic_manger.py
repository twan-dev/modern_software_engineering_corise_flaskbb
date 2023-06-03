import pytest

from flaskbb.forum.topic_manager import TopicManager
# CoRise TODO: add unit tests for topic manager

class TestTopicManager(object):

    def test_set_lock_state(user, topic):
        subject = TopicManager(user, [topic])
        result = subject.set_lock_state(True)

        assert result == 1
        assert topic.locked == True

    def test_set_lock_state_doesnot_modify_topic_with_desired_state(user, topic_locked):
        subject = TopicManager(user, [topic_locked])
        result = subject.set_lock_state(True)

        assert result == 0

    def test_set_lock_state_handles_each_topic(user, topic, topic_locked):
        subject = TopicManager(user, [topic_locked, topic])
        result = subject.set_lock_state(False)

        assert result == 1

    def test_set_imporant_state(user, topic):
        subject = TopicManager(user, [topic])
        result = subject.set_important_state(True)

        assert result == 1
        assert topic.important == True

    def test_set_imporant_state_handles_each_topic(user, topic, topic_important):
        subject = TopicManager(user, [topic_important, topic])
        result = subject.set_important_state(False)

        assert result == 1
        assert topic_important.important == False
        