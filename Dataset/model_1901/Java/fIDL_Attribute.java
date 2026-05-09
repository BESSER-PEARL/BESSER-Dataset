





import java.util.List;
import java.util.ArrayList;

public class fIDL_Attribute  {

    private String name;
    private String value;





    private fIDL_AttributedDeclaration fidl_attributeddeclaration;


    public fIDL_Attribute(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public fIDL_AttributedDeclaration getFidl_attributeddeclaration() {
        return fidl_attributeddeclaration;
    }

    public void setFidl_attributeddeclaration(fIDL_AttributedDeclaration fidl_attributeddeclaration) {
        this.fidl_attributeddeclaration = fidl_attributeddeclaration;
    }

}