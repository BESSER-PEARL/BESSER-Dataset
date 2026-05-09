





import java.util.List;
import java.util.ArrayList;

public class ccsl_complexType_DeclaredType extends datatype_ObjectType, namedElements_NamedElement, import_ImportableElement {

    private String visibility;
    private String static;



    public ccsl_complexType_DeclaredType(
        String visibility,        String static    ) {
        super(
        );
        this.visibility = visibility;
        this.static = static;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }


}