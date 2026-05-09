





import java.util.List;
import java.util.ArrayList;

public class mtl_ModuleElement extends utilities_ASTNode, ENamedElement {

    private String visibility;





    private mtl_Module mtl_module;


    public mtl_ModuleElement(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public mtl_Module getMtl_module() {
        return mtl_module;
    }

    public void setMtl_module(mtl_Module mtl_module) {
        this.mtl_module = mtl_module;
    }

}