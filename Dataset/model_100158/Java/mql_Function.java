





import java.util.List;
import java.util.ArrayList;

public class mql_Function  {

    private String name;





    private List<mql_Variable> mql_variables;


    public mql_Function(
        String name    ) {
        this.name = name;
        this.mql_variables = new ArrayList<>();
    }

    public mql_Function(
        String name        ArrayList<mql_Variable> mql_variables    ) {
        this.name = name;
        this.mql_variables = mql_variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mql_Variable> getMql_variables() {
        return mql_variables;
    }

    public void addMql_variable(Mql_variable mql_variable) {
        this.mql_variables.add(mql_variable);
    }

}