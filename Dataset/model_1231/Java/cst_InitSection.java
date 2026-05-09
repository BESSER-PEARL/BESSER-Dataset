





import java.util.List;
import java.util.ArrayList;

public class cst_InitSection extends CSTNode {






    private List<cst_Variable> cst_variables;


    public cst_InitSection(
    ) {
        super(
        );
        this.cst_variables = new ArrayList<>();
    }

    public cst_InitSection(
        ArrayList<cst_Variable> cst_variables    ) {
        this.cst_variables = cst_variables;
    }


    public List<cst_Variable> getCst_variables() {
        return cst_variables;
    }

    public void addCst_variable(Cst_variable cst_variable) {
        this.cst_variables.add(cst_variable);
    }

}