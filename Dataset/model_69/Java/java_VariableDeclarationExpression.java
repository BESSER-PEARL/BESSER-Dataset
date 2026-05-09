





import java.util.List;
import java.util.ArrayList;

public class java_VariableDeclarationExpression extends AbstractVariablesContainer, Expression {






    private List<java_Annotation> java_annotations;


    public java_VariableDeclarationExpression(
    ) {
        super(
        );
        this.java_annotations = new ArrayList<>();
    }

    public java_VariableDeclarationExpression(
        ArrayList<java_Annotation> java_annotations    ) {
        this.java_annotations = java_annotations;
    }


    public List<java_Annotation> getJava_annotations() {
        return java_annotations;
    }

    public void addJava_annotation(Java_annotation java_annotation) {
        this.java_annotations.add(java_annotation);
    }

}