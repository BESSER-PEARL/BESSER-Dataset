





import java.util.List;
import java.util.ArrayList;

public class dependencies_Domain extends NamedElement {






    private dependencies_Required dependencies_required;




    private dependencies_EPackage dependencies_epackage;




    private dependencies_Graph dependencies_graph;


    public dependencies_Domain(
    ) {
        super(
        );
    }



    public dependencies_Required getDependencies_required() {
        return dependencies_required;
    }

    public void setDependencies_required(dependencies_Required dependencies_required) {
        this.dependencies_required = dependencies_required;
    }
    public dependencies_EPackage getDependencies_epackage() {
        return dependencies_epackage;
    }

    public void setDependencies_epackage(dependencies_EPackage dependencies_epackage) {
        this.dependencies_epackage = dependencies_epackage;
    }
    public dependencies_Graph getDependencies_graph() {
        return dependencies_graph;
    }

    public void setDependencies_graph(dependencies_Graph dependencies_graph) {
        this.dependencies_graph = dependencies_graph;
    }

}