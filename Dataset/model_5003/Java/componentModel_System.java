





import java.util.List;
import java.util.ArrayList;

public class componentModel_System  {






    private List<componentModel_Interface> componentmodel_interfaces;




    private List<componentModel_AssemblyContext> componentmodel_assemblycontexts;


    public componentModel_System(
    ) {
        this.componentmodel_interfaces = new ArrayList<>();
        this.componentmodel_assemblycontexts = new ArrayList<>();
    }

    public componentModel_System(
        ArrayList<componentModel_Interface> componentmodel_interfaces,        ArrayList<componentModel_AssemblyContext> componentmodel_assemblycontexts    ) {
        this.componentmodel_interfaces = componentmodel_interfaces;
        this.componentmodel_assemblycontexts = componentmodel_assemblycontexts;
    }


    public List<componentModel_Interface> getComponentmodel_interfaces() {
        return componentmodel_interfaces;
    }

    public void addComponentmodel_interface(Componentmodel_interface componentmodel_interface) {
        this.componentmodel_interfaces.add(componentmodel_interface);
    }
    public List<componentModel_AssemblyContext> getComponentmodel_assemblycontexts() {
        return componentmodel_assemblycontexts;
    }

    public void addComponentmodel_assemblycontext(Componentmodel_assemblycontext componentmodel_assemblycontext) {
        this.componentmodel_assemblycontexts.add(componentmodel_assemblycontext);
    }

}