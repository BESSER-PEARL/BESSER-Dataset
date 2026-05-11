





import java.util.List;
import java.util.ArrayList;

public class dependencies_RightTerm extends Term {

    private String value;





    private dependencies_Operation dependencies_operation;




    private dependencies_Edge dependencies_edge;




    private dependencies_Operation dependencies_operation;




    private List<dependencies_SimpleTerm> dependencies_simpleterms;


    public dependencies_RightTerm(
        String value    ) {
        super(
        );
        this.value = value;
        this.dependencies_simpleterms = new ArrayList<>();
    }

    public dependencies_RightTerm(
        String value        ArrayList<dependencies_SimpleTerm> dependencies_simpleterms    ) {
        this.value = value;
        this.dependencies_simpleterms = dependencies_simpleterms;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public dependencies_Operation getDependencies_operation() {
        return dependencies_operation;
    }

    public void setDependencies_operation(dependencies_Operation dependencies_operation) {
        this.dependencies_operation = dependencies_operation;
    }
    public dependencies_Edge getDependencies_edge() {
        return dependencies_edge;
    }

    public void setDependencies_edge(dependencies_Edge dependencies_edge) {
        this.dependencies_edge = dependencies_edge;
    }
    public dependencies_Operation getDependencies_operation() {
        return dependencies_operation;
    }

    public void setDependencies_operation(dependencies_Operation dependencies_operation) {
        this.dependencies_operation = dependencies_operation;
    }
    public List<dependencies_SimpleTerm> getDependencies_simpleterms() {
        return dependencies_simpleterms;
    }

    public void addDependencies_simpleterm(Dependencies_simpleterm dependencies_simpleterm) {
        this.dependencies_simpleterms.add(dependencies_simpleterm);
    }

}