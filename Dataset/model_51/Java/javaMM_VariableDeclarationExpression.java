





import java.util.List;
import java.util.ArrayList;

public class javaMM_VariableDeclarationExpression extends Expression, AbstractVariablesContainer {






    private List<javaMM_Annotation> javamm_annotations;


    public javaMM_VariableDeclarationExpression(
    ) {
        super(
        );
        this.javamm_annotations = new ArrayList<>();
    }

    public javaMM_VariableDeclarationExpression(
        ArrayList<javaMM_Annotation> javamm_annotations    ) {
        this.javamm_annotations = javamm_annotations;
    }


    public List<javaMM_Annotation> getJavamm_annotations() {
        return javamm_annotations;
    }

    public void addJavamm_annotation(Javamm_annotation javamm_annotation) {
        this.javamm_annotations.add(javamm_annotation);
    }

}