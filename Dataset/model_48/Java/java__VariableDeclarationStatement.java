





import java.util.List;
import java.util.ArrayList;

public class java__VariableDeclarationStatement extends AbstractVariablesContainer, Statement {

    private int extraArrayDimensions;





    private List<java__Annotation> java__annotations;




    private java__Modifier java__modifier;




    private java__Modifier java__modifier;


    public java__VariableDeclarationStatement(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java__annotations = new ArrayList<>();
    }

    public java__VariableDeclarationStatement(
        int extraArrayDimensions        ArrayList<java__Annotation> java__annotations    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java__annotations = java__annotations;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public List<java__Annotation> getJava__annotations() {
        return java__annotations;
    }

    public void addJava__annotation(Java__annotation java__annotation) {
        this.java__annotations.add(java__annotation);
    }
    public java__Modifier getJava__modifier() {
        return java__modifier;
    }

    public void setJava__modifier(java__Modifier java__modifier) {
        this.java__modifier = java__modifier;
    }
    public java__Modifier getJava__modifier() {
        return java__modifier;
    }

    public void setJava__modifier(java__Modifier java__modifier) {
        this.java__modifier = java__modifier;
    }

}