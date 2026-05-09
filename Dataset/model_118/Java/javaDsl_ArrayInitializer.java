





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ArrayInitializer extends VariableInitializer {






    private List<javaDsl_VariableInitializer> javadsl_variableinitializers;


    public javaDsl_ArrayInitializer(
    ) {
        super(
        );
        this.javadsl_variableinitializers = new ArrayList<>();
    }

    public javaDsl_ArrayInitializer(
        ArrayList<javaDsl_VariableInitializer> javadsl_variableinitializers    ) {
        this.javadsl_variableinitializers = javadsl_variableinitializers;
    }


    public List<javaDsl_VariableInitializer> getJavadsl_variableinitializers() {
        return javadsl_variableinitializers;
    }

    public void addJavadsl_variableinitializer(Javadsl_variableinitializer javadsl_variableinitializer) {
        this.javadsl_variableinitializers.add(javadsl_variableinitializer);
    }

}