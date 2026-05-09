





import java.util.List;
import java.util.ArrayList;

public class Implementation_RoomComponent_RoomHandler extends RoomComponent_IRoomInformation, RoomComponent_IRoomAdministration {






    private Implementation_StaffComponent_IAuthentication implementation_staffcomponent_iauthentication;


    public Implementation_RoomComponent_RoomHandler(
    ) {
        super(
        );
    }



    public Implementation_StaffComponent_IAuthentication getImplementation_staffcomponent_iauthentication() {
        return implementation_staffcomponent_iauthentication;
    }

    public void setImplementation_staffcomponent_iauthentication(Implementation_StaffComponent_IAuthentication implementation_staffcomponent_iauthentication) {
        this.implementation_staffcomponent_iauthentication = implementation_staffcomponent_iauthentication;
    }

}