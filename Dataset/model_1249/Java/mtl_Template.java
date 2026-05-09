





import java.util.List;
import java.util.ArrayList;

public class mtl_Template extends ModuleElement, Block, DocumentedElement {

    private boolean main;





    private mtl_Template mtl_template;




    private mtl_TemplateInvocation mtl_templateinvocation;




    private List<Variable> variables;


    public mtl_Template(
        boolean main    ) {
        super(
        );
        this.main = main;
        this.variables = new ArrayList<>();
    }

    public mtl_Template(
        boolean main        ArrayList<Variable> variables    ) {
        this.main = main;
        this.variables = variables;
    }

    public boolean getMain() {
        return main;
    }

    public void setMain(boolean main) {
        this.main = main;
    }

    public mtl_Template getMtl_template() {
        return mtl_template;
    }

    public void setMtl_template(mtl_Template mtl_template) {
        this.mtl_template = mtl_template;
    }
    public mtl_TemplateInvocation getMtl_templateinvocation() {
        return mtl_templateinvocation;
    }

    public void setMtl_templateinvocation(mtl_TemplateInvocation mtl_templateinvocation) {
        this.mtl_templateinvocation = mtl_templateinvocation;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}