





import java.util.List;
import java.util.ArrayList;

public class build_CompoundBuildUnitRepository extends BuildUnitRepository {






    private List<build_IBuildUnitRepository> build_ibuildunitrepositorys;


    public build_CompoundBuildUnitRepository(
    ) {
        super(
        );
        this.build_ibuildunitrepositorys = new ArrayList<>();
    }

    public build_CompoundBuildUnitRepository(
        ArrayList<build_IBuildUnitRepository> build_ibuildunitrepositorys    ) {
        this.build_ibuildunitrepositorys = build_ibuildunitrepositorys;
    }


    public List<build_IBuildUnitRepository> getBuild_ibuildunitrepositorys() {
        return build_ibuildunitrepositorys;
    }

    public void addBuild_ibuildunitrepository(Build_ibuildunitrepository build_ibuildunitrepository) {
        this.build_ibuildunitrepositorys.add(build_ibuildunitrepository);
    }

}