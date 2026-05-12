





import java.util.List;
import java.util.ArrayList;

public class jpql_Function  {

    private String name;





    private List<jpql_Variable> jpql_variables;


    public jpql_Function(
        String name    ) {
        this.name = name;
        this.jpql_variables = new ArrayList<>();
    }

    public jpql_Function(
        String name        ArrayList<jpql_Variable> jpql_variables    ) {
        this.name = name;
        this.jpql_variables = jpql_variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<jpql_Variable> getJpql_variables() {
        return jpql_variables;
    }

    public void addJpql_variable(Jpql_variable jpql_variable) {
        this.jpql_variables.add(jpql_variable);
    }

}