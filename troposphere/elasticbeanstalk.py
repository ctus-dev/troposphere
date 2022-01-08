# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.elasticbeanstalk import WebServer  # noqa: F401
from .validators.elasticbeanstalk import WebServerType  # noqa: F401
from .validators.elasticbeanstalk import Worker  # noqa: F401
from .validators.elasticbeanstalk import WorkerType  # noqa: F401
from .validators.elasticbeanstalk import validate_tier_name, validate_tier_type


class MaxAgeRule(AWSProperty):
    """
    `MaxAgeRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html>`__
    """

    props: PropsDictType = {
        "DeleteSourceFromS3": (boolean, False),
        "Enabled": (boolean, False),
        "MaxAgeInDays": (integer, False),
    }


class MaxCountRule(AWSProperty):
    """
    `MaxCountRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html>`__
    """

    props: PropsDictType = {
        "DeleteSourceFromS3": (boolean, False),
        "Enabled": (boolean, False),
        "MaxCount": (integer, False),
    }


class ApplicationVersionLifecycleConfig(AWSProperty):
    """
    `ApplicationVersionLifecycleConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html>`__
    """

    props: PropsDictType = {
        "MaxAgeRule": (MaxAgeRule, False),
        "MaxCountRule": (MaxCountRule, False),
    }


class ApplicationResourceLifecycleConfig(AWSProperty):
    """
    `ApplicationResourceLifecycleConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html>`__
    """

    props: PropsDictType = {
        "ServiceRole": (str, False),
        "VersionLifecycleConfig": (ApplicationVersionLifecycleConfig, False),
    }


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html>`__
    """

    resource_type = "AWS::ElasticBeanstalk::Application"

    props: PropsDictType = {
        "ApplicationName": (str, False),
        "Description": (str, False),
        "ResourceLifecycleConfig": (ApplicationResourceLifecycleConfig, False),
    }


class SourceBundle(AWSProperty):
    """
    `SourceBundle <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html>`__
    """

    props: PropsDictType = {
        "S3Bucket": (str, True),
        "S3Key": (str, True),
    }


class ApplicationVersion(AWSObject):
    """
    `ApplicationVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html>`__
    """

    resource_type = "AWS::ElasticBeanstalk::ApplicationVersion"

    props: PropsDictType = {
        "ApplicationName": (str, True),
        "Description": (str, False),
        "SourceBundle": (SourceBundle, True),
    }


class OptionSetting(AWSProperty):
    """
    `OptionSetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html>`__
    """

    props: PropsDictType = {
        "Namespace": (str, True),
        "OptionName": (str, True),
        "ResourceName": (str, False),
        "Value": (str, False),
    }


class SourceConfiguration(AWSProperty):
    """
    `SourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "ApplicationName": (str, True),
        "TemplateName": (str, True),
    }


class ConfigurationTemplate(AWSObject):
    """
    `ConfigurationTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html>`__
    """

    resource_type = "AWS::ElasticBeanstalk::ConfigurationTemplate"

    props: PropsDictType = {
        "ApplicationName": (str, True),
        "Description": (str, False),
        "EnvironmentId": (str, False),
        "OptionSettings": ([OptionSetting], False),
        "PlatformArn": (str, False),
        "SolutionStackName": (str, False),
        "SourceConfiguration": (SourceConfiguration, False),
    }


class Tier(AWSProperty):
    """
    `Tier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html>`__
    """

    props: PropsDictType = {
        "Name": (validate_tier_name, False),
        "Type": (validate_tier_type, False),
        "Version": (str, False),
    }


class Environment(AWSObject):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html>`__
    """

    resource_type = "AWS::ElasticBeanstalk::Environment"

    props: PropsDictType = {
        "ApplicationName": (str, True),
        "CNAMEPrefix": (str, False),
        "Description": (str, False),
        "EnvironmentName": (str, False),
        "OperationsRole": (str, False),
        "OptionSettings": ([OptionSetting], False),
        "PlatformArn": (str, False),
        "SolutionStackName": (str, False),
        "Tags": (Tags, False),
        "TemplateName": (str, False),
        "Tier": (Tier, False),
        "VersionLabel": (str, False),
    }
