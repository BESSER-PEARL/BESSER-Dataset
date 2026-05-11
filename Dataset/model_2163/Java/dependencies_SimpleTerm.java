





import java.util.List;
import java.util.ArrayList;

public class dependencies_SimpleTerm extends Term {






    private dependencies_CoreClass dependencies_coreclass;




    private dependencies_EClass dependencies_eclass;




    private dependencies_Edge dependencies_edge;


    public dependencies_SimpleTerm(
    ) {
        super(
        );
    }



    public dependencies_CoreClass getDependencies_coreclass() {
        return dependencies_coreclass;
    }

    public void setDependencies_coreclass(dependencies_CoreClass dependencies_coreclass) {
        this.dependencies_coreclass = dependencies_coreclass;
    }
    public dependencies_EClass getDependencies_eclass() {
        return dependencies_eclass;
    }

    public void setDependencies_eclass(dependencies_EClass dependencies_eclass) {
        this.dependencies_eclass = dependencies_eclass;
    }
    public dependencies_Edge getDependencies_edge() {
        return dependencies_edge;
    }

    public void setDependencies_edge(dependencies_Edge dependencies_edge) {
        this.dependencies_edge = dependencies_edge;
    }

}