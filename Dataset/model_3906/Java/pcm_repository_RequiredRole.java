





import java.util.List;
import java.util.ArrayList;

public class pcm_repository_RequiredRole extends Role {






    private Interface interface;




    private entity_InterfaceRequiringEntity entity_interfacerequiringentity;


    public pcm_repository_RequiredRole(
    ) {
        super(
        );
    }



    public Interface getInterface() {
        return interface;
    }

    public void setInterface(Interface interface) {
        this.interface = interface;
    }
    public entity_InterfaceRequiringEntity getEntity_interfacerequiringentity() {
        return entity_interfacerequiringentity;
    }

    public void setEntity_interfacerequiringentity(entity_InterfaceRequiringEntity entity_interfacerequiringentity) {
        this.entity_interfacerequiringentity = entity_interfacerequiringentity;
    }

}