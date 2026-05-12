





import java.util.List;
import java.util.ArrayList;

public class build_BeeModel extends BChainedExpression, IBuildUnitContainer {






    private List<build_FirstFoundUnitProvider> build_firstfoundunitproviders;




    private List<build_Repository> build_repositorys;


    public build_BeeModel(
    ) {
        super(
        );
        this.build_firstfoundunitproviders = new ArrayList<>();
        this.build_repositorys = new ArrayList<>();
    }

    public build_BeeModel(
        ArrayList<build_FirstFoundUnitProvider> build_firstfoundunitproviders,        ArrayList<build_Repository> build_repositorys    ) {
        this.build_firstfoundunitproviders = build_firstfoundunitproviders;
        this.build_repositorys = build_repositorys;
    }


    public List<build_FirstFoundUnitProvider> getBuild_firstfoundunitproviders() {
        return build_firstfoundunitproviders;
    }

    public void addBuild_firstfoundunitprovider(Build_firstfoundunitprovider build_firstfoundunitprovider) {
        this.build_firstfoundunitproviders.add(build_firstfoundunitprovider);
    }
    public List<build_Repository> getBuild_repositorys() {
        return build_repositorys;
    }

    public void addBuild_repository(Build_repository build_repository) {
        this.build_repositorys.add(build_repository);
    }

}