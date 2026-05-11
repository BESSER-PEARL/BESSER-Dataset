





import java.util.List;
import java.util.ArrayList;

public class componentModel_ProvidedDelegationConnector extends DelegationConnector {






    private componentModel_Interface componentmodel_interface;




    private componentModel_ProvidedRole componentmodel_providedrole;


    public componentModel_ProvidedDelegationConnector(
    ) {
        super(
        );
    }



    public componentModel_Interface getComponentmodel_interface() {
        return componentmodel_interface;
    }

    public void setComponentmodel_interface(componentModel_Interface componentmodel_interface) {
        this.componentmodel_interface = componentmodel_interface;
    }
    public componentModel_ProvidedRole getComponentmodel_providedrole() {
        return componentmodel_providedrole;
    }

    public void setComponentmodel_providedrole(componentModel_ProvidedRole componentmodel_providedrole) {
        this.componentmodel_providedrole = componentmodel_providedrole;
    }

}