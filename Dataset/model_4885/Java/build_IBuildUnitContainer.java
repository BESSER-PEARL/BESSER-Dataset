





import java.util.List;
import java.util.ArrayList;

public class build_IBuildUnitContainer  {






    private List<build_BuildUnit> build_buildunits;




    private build_BuildUnit build_buildunit;


    public build_IBuildUnitContainer(
    ) {
        this.build_buildunits = new ArrayList<>();
    }

    public build_IBuildUnitContainer(
        ArrayList<build_BuildUnit> build_buildunits    ) {
        this.build_buildunits = build_buildunits;
    }


    public List<build_BuildUnit> getBuild_buildunits() {
        return build_buildunits;
    }

    public void addBuild_buildunit(Build_buildunit build_buildunit) {
        this.build_buildunits.add(build_buildunit);
    }
    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }

}