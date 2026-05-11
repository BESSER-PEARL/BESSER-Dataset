





import java.util.List;
import java.util.ArrayList;

public class vql_Type  {

    private String typename;





    private vql_Variable vql_variable;


    public vql_Type(
        String typename    ) {
        this.typename = typename;
    }


    public String getTypename() {
        return typename;
    }

    public void setTypename(String typename) {
        this.typename = typename;
    }

    public vql_Variable getVql_variable() {
        return vql_variable;
    }

    public void setVql_variable(vql_Variable vql_variable) {
        this.vql_variable = vql_variable;
    }

}