





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmAnnotationAnnotationValue extends JvmAnnotationValue {






    private List<JvmAnnotationReference> jvmannotationreferences;


    public model_types_JvmAnnotationAnnotationValue(
    ) {
        super(
        );
        this.jvmannotationreferences = new ArrayList<>();
    }

    public model_types_JvmAnnotationAnnotationValue(
        ArrayList<JvmAnnotationReference> jvmannotationreferences    ) {
        this.jvmannotationreferences = jvmannotationreferences;
    }


    public List<JvmAnnotationReference> getJvmannotationreferences() {
        return jvmannotationreferences;
    }

    public void addJvmannotationreference(Jvmannotationreference jvmannotationreference) {
        this.jvmannotationreferences.add(jvmannotationreference);
    }

}