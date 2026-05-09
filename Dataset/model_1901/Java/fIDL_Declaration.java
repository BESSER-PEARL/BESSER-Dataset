





import java.util.List;
import java.util.ArrayList;

public class fIDL_Declaration  {

    private String name;





    private fIDL_AttributedDeclaration fidl_attributeddeclaration;


    public fIDL_Declaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fIDL_AttributedDeclaration getFidl_attributeddeclaration() {
        return fidl_attributeddeclaration;
    }

    public void setFidl_attributeddeclaration(fIDL_AttributedDeclaration fidl_attributeddeclaration) {
        this.fidl_attributeddeclaration = fidl_attributeddeclaration;
    }

}