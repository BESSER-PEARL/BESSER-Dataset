





import java.util.List;
import java.util.ArrayList;

public class cst_ModuleImportsValue extends CSTNode {

    private String name;





    private cst_Module cst_module;


    public cst_ModuleImportsValue(
        String name    ) {
        super(
        );
        this.name = name;
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