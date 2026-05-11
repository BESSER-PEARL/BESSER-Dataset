





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmEnumAnnotationValue extends JvmAnnotationValue {






    private List<JvmEnumerationLiteral> jvmenumerationliterals;


    public model_types_JvmEnumAnnotationValue(
    ) {
        super(
        );
        this.jvmenumerationliterals = new ArrayList<>();
    }

    public model_types_JvmEnumAnnotationValue(
        ArrayList<JvmEnumerationLiteral> jvmenumerationliterals    ) {
        this.jvmenumerationliterals = jvmenumerationliterals;
    }


    public List<JvmEnumerationLiteral> getJvmenumerationliterals() {
        return jvmenumerationliterals;
    }

    public void addJvmenumerationliteral(Jvmenumerationliteral jvmenumerationliteral) {
        this.jvmenumerationliterals.add(jvmenumerationliteral);
    }

}