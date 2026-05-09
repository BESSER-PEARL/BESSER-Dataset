





import java.util.List;
import java.util.ArrayList;

public class javaDsl_Expression extends ConstantExpression, PrimaryNoNewArray {






    private javaDsl_VariableInitializer javadsl_variableinitializer;


    public javaDsl_Expression(
    ) {
        super(
        );
    }



    public javaDsl_VariableInitializer getJavadsl_variableinitializer() {
        return javadsl_variableinitializer;
    }

    public void setJavadsl_variableinitializer(javaDsl_VariableInitializer javadsl_variableinitializer) {
        this.javadsl_variableinitializer = javadsl_variableinitializer;
    }

}