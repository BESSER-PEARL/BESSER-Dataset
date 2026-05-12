





import java.util.List;
import java.util.ArrayList;

public class build_Synchronization  {






    private List<build_BuilderQuery> build_builderquerys;




    private build_BuildUnit build_buildunit;


    public build_Synchronization(
    ) {
        this.build_builderquerys = new ArrayList<>();
    }

    public build_Synchronization(
        ArrayList<build_BuilderQuery> build_builderquerys    ) {
        this.build_builderquerys = build_builderquerys;
    }


    public List<build_BuilderQuery> getBuild_builderquerys() {
        return build_builderquerys;
    }

    public void addBuild_builderquery(Build_builderquery build_builderquery) {
        this.build_builderquerys.add(build_builderquery);
    }
    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }

}