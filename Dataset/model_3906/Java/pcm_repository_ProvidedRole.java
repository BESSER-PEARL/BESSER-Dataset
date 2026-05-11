





import java.util.List;
import java.util.ArrayList;

public class pcm_repository_ProvidedRole extends Role {






    private entity_InterfaceProvidingEntity entity_interfaceprovidingentity;




    private Interface interface;


    public pcm_repository_ProvidedRole(
    ) {
        super(
        );
    }



    public entity_InterfaceProvidingEntity getEntity_interfaceprovidingentity() {
        return entity_interfaceprovidingentity;
    }

    public void setEntity_interfaceprovidingentity(entity_InterfaceProvidingEntity entity_interfaceprovidingentity) {
        this.entity_interfaceprovidingentity = entity_interfaceprovidingentity;
    }
    public Interface getInterface() {
        return interface;
    }

    public void setInterface(Interface interface) {
        this.interface = interface;
    }

}