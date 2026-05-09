





import java.util.List;
import java.util.ArrayList;

public class Java_VariableDeclarationStatement extends Statement, AbstractVariablesContainer {

    private int extraArrayDimensions;





    private Java_Modifier java_modifier;




    private List<Java_Annotation> java_annotations;




    private Java_Modifier java_modifier;


    public Java_VariableDeclarationStatement(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_annotations = new ArrayList<>();
    }

    public Java_VariableDeclarationStatement(
        int extraArrayDimensions        ArrayList<Java_Annotation> java_annotations    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_annotations = java_annotations;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
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
    public Java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(Java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }

}