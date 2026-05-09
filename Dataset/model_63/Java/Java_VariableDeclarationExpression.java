





import java.util.List;
import java.util.ArrayList;

public class Java_VariableDeclarationExpression extends Expression, AbstractVariablesContainer {






    private Java_Modifier java_modifier;




    private Java_Modifier java_modifier;




    private List<Java_Annotation> java_annotations;


    public Java_VariableDeclarationExpression(
    ) {
        super(
        );
        this.java_annotations = new ArrayList<>();
    }

    public Java_VariableDeclarationExpression(
        ArrayList<Java_Annotation> java_annotations    ) {
        this.java_annotations = java_annotations;
    }


    public Java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(Java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }
    public Java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(Java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }
    public List<Java_Annotation> getJava_annotations() {
        return java_annotations;
    }

    public void addJava_annotation(Java_annotation java_annotation) {
        this.java_annotations.add(java_annotation);
    }

}