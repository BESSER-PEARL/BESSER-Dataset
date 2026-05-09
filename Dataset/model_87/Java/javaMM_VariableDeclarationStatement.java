





import java.util.List;
import java.util.ArrayList;

public class javaMM_VariableDeclarationStatement extends Statement, AbstractVariablesContainer {

    private int extraArrayDimensions;





    private javaMM_Modifier javamm_modifier;




    private List<javaMM_Annotation> javamm_annotations;




    private javaMM_Modifier javamm_modifier;


    public javaMM_VariableDeclarationStatement(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.javamm_annotations = new ArrayList<>();
    }

    public javaMM_VariableDeclarationStatement(
        int extraArrayDimensions        ArrayList<javaMM_Annotation> javamm_annotations    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.javamm_annotations = javamm_annotations;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public javaMM_Modifier getJavamm_modifier() {
        return javamm_modifier;
    }

    public void setJavamm_modifier(javaMM_Modifier javamm_modifier) {
        this.javamm_modifier = javamm_modifier;
    }
    public List<javaMM_Annotation> getJavamm_annotations() {
        return javamm_annotations;
    }

    public void addJavamm_annotation(Javamm_annotation javamm_annotation) {
        this.javamm_annotations.add(javamm_annotation);
    }
    public javaMM_Modifier getJavamm_modifier() {
        return javamm_modifier;
    }

    public void setJavamm_modifier(javaMM_Modifier javamm_modifier) {
        this.javamm_modifier = javamm_modifier;
    }

}