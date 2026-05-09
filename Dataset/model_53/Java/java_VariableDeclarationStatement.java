





import java.util.List;
import java.util.ArrayList;

public class java_VariableDeclarationStatement extends Statement, AbstractVariablesContainer {

    private int extraArrayDimensions;





    private List<java_Annotation> java_annotations;




    private java_Modifier java_modifier;




    private java_Modifier java_modifier;


    public java_VariableDeclarationStatement(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_annotations = new ArrayList<>();
    }

    public java_VariableDeclarationStatement(
        int extraArrayDimensions        ArrayList<java_Annotation> java_annotations    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_annotations = java_annotations;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public List<java_Annotation> getJava_annotations() {
        return java_annotations;
    }

    public void addJava_annotation(Java_annotation java_annotation) {
        this.java_annotations.add(java_annotation);
    }
    public java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }
    public java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }

}