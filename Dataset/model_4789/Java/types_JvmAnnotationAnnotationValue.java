





import java.util.List;
import java.util.ArrayList;

public class types_JvmAnnotationAnnotationValue extends JvmAnnotationValue {






    private List<types_JvmAnnotationReference> types_jvmannotationreferences;


    public types_JvmAnnotationAnnotationValue(
    ) {
        super(
        );
        this.types_jvmannotationreferences = new ArrayList<>();
    }

    public types_JvmAnnotationAnnotationValue(
        ArrayList<types_JvmAnnotationReference> types_jvmannotationreferences    ) {
        this.types_jvmannotationreferences = types_jvmannotationreferences;
    }


    public List<types_JvmAnnotationReference> getTypes_jvmannotationreferences() {
        return types_jvmannotationreferences;
    }

    public void addTypes_jvmannotationreference(Types_jvmannotationreference types_jvmannotationreference) {
        this.types_jvmannotationreferences.add(types_jvmannotationreference);
    }

}