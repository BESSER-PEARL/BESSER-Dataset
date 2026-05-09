





import java.util.List;
import java.util.ArrayList;

public class mtl_Template extends ModuleElement, Block, DocumentedElement {

    private boolean main;





    private List<mtl_Template> mtl_templates;


    public mtl_Template(
        boolean main    ) {
        super(
        );
        this.main = main;
        this.mtl_templates = new ArrayList<>();
    }

    public mtl_Template(
        boolean main        ArrayList<mtl_Template> mtl_templates    ) {
        this.main = main;
        this.mtl_templates = mtl_templates;
    }

    public boolean getMain() {
        return main;
    }

    public void setMain(boolean main) {
        this.main = main;
    }

    public List<mtl_Template> getMtl_templates() {
        return mtl_templates;
    }

    public void addMtl_template(Mtl_template mtl_template) {
        this.mtl_templates.add(mtl_template);
    }

}