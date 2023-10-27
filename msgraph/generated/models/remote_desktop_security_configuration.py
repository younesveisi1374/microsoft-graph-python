from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .target_device_group import TargetDeviceGroup

from .entity import Entity

@dataclass
class RemoteDesktopSecurityConfiguration(Entity):
    # The isRemoteDesktopProtocolEnabled property
    is_remote_desktop_protocol_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The targetDeviceGroups property
    target_device_groups: Optional[List[TargetDeviceGroup]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteDesktopSecurityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteDesktopSecurityConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RemoteDesktopSecurityConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .target_device_group import TargetDeviceGroup

        from .entity import Entity
        from .target_device_group import TargetDeviceGroup

        fields: Dict[str, Callable[[Any], None]] = {
            "isRemoteDesktopProtocolEnabled": lambda n : setattr(self, 'is_remote_desktop_protocol_enabled', n.get_bool_value()),
            "targetDeviceGroups": lambda n : setattr(self, 'target_device_groups', n.get_collection_of_object_values(TargetDeviceGroup)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("isRemoteDesktopProtocolEnabled", self.is_remote_desktop_protocol_enabled)
        writer.write_collection_of_object_values("targetDeviceGroups", self.target_device_groups)
    

