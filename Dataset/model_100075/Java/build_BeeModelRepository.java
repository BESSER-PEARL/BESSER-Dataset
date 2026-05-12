





import java.util.List;
import java.util.ArrayList;

public class build_BeeModelRepository extends BuildUnitRepository {






    private List<build_BeeModel> build_beemodels;


    public build_BeeModelRepository(
    ) {
        super(
        );
        this.build_beemodels = new ArrayList<>();
    }

    public build_BeeModelRepository(
        ArrayList<build_BeeModel> build_beemodels    ) {
        this.build_beemodels = build_beemodels;
    }


    public List<build_BeeModel> getBuild_beemodels() {
        return build_beemodels;
    }

    public void addBuild_beemodel(Build_beemodel build_beemodel) {
        this.build_beemodels.add(build_beemodel);
    }

}