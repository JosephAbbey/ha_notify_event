# Notify Event

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![Community Forum][forum-shield]][forum]

_Integration to integrate with [notify_event][notify_event]._

**This integration will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from blueprint API.
`switch` | Switch something `True` or `False`.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `notify_event`.
1. Download _all_ the files from the `custom_components/notify_event/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Integration blueprint"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[notify_event]: https://github.com/josephabbey/ha_notify_event
[commits-shield]: https://img.shields.io/github/commit-activity/y/josephabbey/ha_notify_event.svg?style=for-the-badge
[commits]: https://github.com/josephabbey/ha_notify_event/commits/main
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/josephabbey/ha_notify_event.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/josephabbey/ha_notify_event.svg?style=for-the-badge
[releases]: https://github.com/josephabbey/ha_notify_event/releases
