"""Event notification service."""

from __future__ import annotations

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TITLE,
    ATTR_TITLE_DEFAULT,
    ATTR_MESSAGE,
    BaseNotificationService,
)
from homeassistant.const import (
    Platform,
    CONF_NAME,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.reload import setup_reload_service
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import (
    DOMAIN,
)

PLATFORMS = [Platform.NOTIFY]


def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> EventNotificationService | None:
    """Get the event notification service."""
    setup_reload_service(hass, DOMAIN, PLATFORMS)
    event_service = EventNotificationService(
        hass,
        config[CONF_NAME],
    )

    return event_service


class EventNotificationService(BaseNotificationService):
    """Implement the notification service for Events."""

    def __init__(self, hass: HomeAssistant, event_id: str):
        """Initialize the service."""
        self._hass = hass
        self.event_id = event_id

    async def async_send_message(self, message="", **kwargs):
        """Send the event."""
        data = {ATTR_MESSAGE: message}

        # Remove default title from notifications.
        if (
            kwargs.get(ATTR_TITLE) is not None
            and kwargs.get(ATTR_TITLE) != ATTR_TITLE_DEFAULT
        ):
            data[ATTR_TITLE] = kwargs.get(ATTR_TITLE)

        if kwargs.get(ATTR_DATA) is not None:
            data[ATTR_DATA] = kwargs.get(ATTR_DATA)

        self._hass.bus.fire("notify." + self.event_id, data)
