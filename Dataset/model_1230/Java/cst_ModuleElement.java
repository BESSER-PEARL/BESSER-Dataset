





import java.util.List;
import java.util.ArrayList;

public class cst_ModuleElement extends CSTNode {

    private String visibility;
    private String name;





    private cst_Module cst_module;


    public cst_ModuleElement(
        String visibility,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cst_Module getCst_module() {
        return cst_module;
    }

    public void setCst_module(cst_Module cst_module) {
        this.cst_module = cst_module;
    }

}