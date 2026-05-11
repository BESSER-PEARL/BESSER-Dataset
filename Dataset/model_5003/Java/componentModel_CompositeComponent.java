





import java.util.List;
import java.util.ArrayList;

public class componentModel_CompositeComponent extends Component {






    private List<componentModel_AssemblyContext> componentmodel_assemblycontexts;


    public componentModel_CompositeComponent(
    ) {
        super(
        );
        this.componentmodel_assemblycontexts = new ArrayList<>();
    }

    public componentModel_CompositeComponent(
        ArrayList<componentModel_AssemblyContext> componentmodel_assemblycontexts    ) {
        this.componentmodel_assemblycontexts = componentmodel_assemblycontexts;
    }


    public List<componentModel_AssemblyContext> getComponentmodel_assemblycontexts() {
        return componentmodel_assemblycontexts;
    }

    public void addComponentmodel_assemblycontext(Componentmodel_assemblycontext componentmodel_assemblycontext) {
        this.componentmodel_assemblycontexts.add(componentmodel_assemblycontext);
    }

}