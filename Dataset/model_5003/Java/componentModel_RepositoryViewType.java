





import java.util.List;
import java.util.ArrayList;

public class componentModel_RepositoryViewType extends ViewType {






    private List<componentModel_Repository> componentmodel_repositorys;


    public componentModel_RepositoryViewType(
    ) {
        super(
        );
        this.componentmodel_repositorys = new ArrayList<>();
    }

    public componentModel_RepositoryViewType(
        ArrayList<componentModel_Repository> componentmodel_repositorys    ) {
        this.componentmodel_repositorys = componentmodel_repositorys;
    }


    public List<componentModel_Repository> getComponentmodel_repositorys() {
        return componentmodel_repositorys;
    }

    public void addComponentmodel_repository(Componentmodel_repository componentmodel_repository) {
        this.componentmodel_repositorys.add(componentmodel_repository);
    }

}