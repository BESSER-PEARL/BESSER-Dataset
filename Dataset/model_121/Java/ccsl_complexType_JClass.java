





import java.util.List;
import java.util.ArrayList;

public class ccsl_complexType_JClass extends complexType_DeclaredType, complexType_ComplexType, annotation_AnnotableElement {

    private String inheritance;



    public ccsl_complexType_JClass(
        String inheritance    ) {
        super(
        );
        this.inheritance = inheritance;
    }


    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }


}