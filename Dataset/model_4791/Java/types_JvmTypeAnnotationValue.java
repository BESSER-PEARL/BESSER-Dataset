





import java.util.List;
import java.util.ArrayList;

public class types_JvmTypeAnnotationValue extends JvmAnnotationValue {






    private List<types_JvmTypeReference> types_jvmtypereferences;


    public types_JvmTypeAnnotationValue(
    ) {
        super(
        );
        this.types_jvmtypereferences = new ArrayList<>();
    }

    public types_JvmTypeAnnotationValue(
        ArrayList<types_JvmTypeReference> types_jvmtypereferences    ) {
        this.types_jvmtypereferences = types_jvmtypereferences;
    }


    public List<types_JvmTypeReference> getTypes_jvmtypereferences() {
        return types_jvmtypereferences;
    }

    public void addTypes_jvmtypereference(Types_jvmtypereference types_jvmtypereference) {
        this.types_jvmtypereferences.add(types_jvmtypereference);
    }

}