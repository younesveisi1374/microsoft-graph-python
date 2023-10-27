from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class OutlookGeoCoordinates(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The accuracy of the latitude and longitude. As an example, the accuracy can be measured in meters, such as the latitude and longitude are accurate to within 50 meters.
    accuracy: Optional[float] = None
    # The altitude of the location.
    altitude: Optional[float] = None
    # The accuracy of the altitude.
    altitude_accuracy: Optional[float] = None
    # The latitude of the location.
    latitude: Optional[float] = None
    # The longitude of the location.
    longitude: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookGeoCoordinates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutlookGeoCoordinates
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OutlookGeoCoordinates()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "accuracy": lambda n : setattr(self, 'accuracy', n.get_float_value()),
            "altitude": lambda n : setattr(self, 'altitude', n.get_float_value()),
            "altitudeAccuracy": lambda n : setattr(self, 'altitude_accuracy', n.get_float_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_float_value("accuracy", self.accuracy)
        writer.write_float_value("altitude", self.altitude)
        writer.write_float_value("altitudeAccuracy", self.altitude_accuracy)
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

