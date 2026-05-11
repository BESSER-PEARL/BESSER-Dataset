





import java.util.List;
import java.util.ArrayList;

public class types_JvmFormalParameter extends JvmIdentifiableElement, JvmAnnotationTarget {

    private String name;





    private types_JvmTypeReference types_jvmtypereference;


    public types_JvmFormalParameter(
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

    public types_JvmTypeReference getTypes_jvmtypereference() {
        return types_jvmtypereference;
    }

    public void setTypes_jvmtypereference(types_JvmTypeReference types_jvmtypereference) {
        this.types_jvmtypereference = types_jvmtypereference;
    }

}