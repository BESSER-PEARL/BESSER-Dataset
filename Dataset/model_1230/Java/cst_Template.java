





import java.util.List;
import java.util.ArrayList;

public class cst_Template extends ModuleElement, Block {






    private List<cst_TemplateOverridesValue> cst_templateoverridesvalues;




    private List<cst_Variable> cst_variables;


    public cst_Template(
    ) {
        super(
        );
        this.cst_templateoverridesvalues = new ArrayList<>();
        this.cst_variables = new ArrayList<>();
    }

    public cst_Template(
        ArrayList<cst_TemplateOverridesValue> cst_templateoverridesvalues,        ArrayList<cst_Variable> cst_variables    ) {
        this.cst_templateoverridesvalues = cst_templateoverridesvalues;
        this.cst_variables = cst_variables;
    }


    public List<cst_TemplateOverridesValue> getCst_templateoverridesvalues() {
        return cst_templateoverridesvalues;
    }

    public void addCst_templateoverridesvalue(Cst_templateoverridesvalue cst_templateoverridesvalue) {
        this.cst_templateoverridesvalues.add(cst_templateoverridesvalue);
    }
    public List<cst_Variable> getCst_variables() {
        return cst_variables;
    }

    public void addCst_variable(Cst_variable cst_variable) {
        this.cst_variables.add(cst_variable);
    }

}