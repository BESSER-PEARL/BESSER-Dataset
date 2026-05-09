





import java.util.List;
import java.util.ArrayList;

public class cst_Query extends ModuleElement {

    private String type;





    private List<cst_Variable> cst_variables;


    public cst_Query(
        String type    ) {
        super(
        );
        this.type = type;
        this.cst_variables = new ArrayList<>();
    }

    public cst_Query(
        String type        ArrayList<cst_Variable> cst_variables    ) {
        this.type = type;
        this.cst_variables = cst_variables;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<cst_Variable> getCst_variables() {
        return cst_variables;
    }

    public void addCst_variable(Cst_variable cst_variable) {
        this.cst_variables.add(cst_variable);
    }

}