





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_CompositeComponent extends Component {






    private List<componentBasedSystem_AssemblyContext> componentbasedsystem_assemblycontexts;




    private List<componentBasedSystem_DelegationConnector> componentbasedsystem_delegationconnectors;


    public componentBasedSystem_CompositeComponent(
    ) {
        super(
        );
        this.componentbasedsystem_assemblycontexts = new ArrayList<>();
        this.componentbasedsystem_delegationconnectors = new ArrayList<>();
    }

    public componentBasedSystem_CompositeComponent(
        ArrayList<componentBasedSystem_AssemblyContext> componentbasedsystem_assemblycontexts,        ArrayList<componentBasedSystem_DelegationConnector> componentbasedsystem_delegationconnectors    ) {
        this.componentbasedsystem_assemblycontexts = componentbasedsystem_assemblycontexts;
        this.componentbasedsystem_delegationconnectors = componentbasedsystem_delegationconnectors;
    }


    public List<componentBasedSystem_AssemblyContext> getComponentbasedsystem_assemblycontexts() {
        return componentbasedsystem_assemblycontexts;
    }

    public void addComponentbasedsystem_assemblycontext(Componentbasedsystem_assemblycontext componentbasedsystem_assemblycontext) {
        this.componentbasedsystem_assemblycontexts.add(componentbasedsystem_assemblycontext);
    }
    public List<componentBasedSystem_DelegationConnector> getComponentbasedsystem_delegationconnectors() {
        return componentbasedsystem_delegationconnectors;
    }

    public void addComponentbasedsystem_delegationconnector(Componentbasedsystem_delegationconnector componentbasedsystem_delegationconnector) {
        this.componentbasedsystem_delegationconnectors.add(componentbasedsystem_delegationconnector);
    }

}