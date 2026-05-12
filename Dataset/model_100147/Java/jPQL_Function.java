





import java.util.List;
import java.util.ArrayList;

public class jPQL_Function  {

    private String name;





    private List<jPQL_Variable> jpql_variables;


    public jPQL_Function(
        String name    ) {
        this.name = name;
        this.jpql_variables = new ArrayList<>();
    }

    public jPQL_Function(
        String name        ArrayList<jPQL_Variable> jpql_variables    ) {
        this.name = name;
        this.jpql_variables = jpql_variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<jPQL_Variable> getJpql_variables() {
        return jpql_variables;
    }

    public void addJpql_variable(Jpql_variable jpql_variable) {
        this.jpql_variables.add(jpql_variable);
    }

}