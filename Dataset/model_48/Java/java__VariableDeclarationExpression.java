





import java.util.List;
import java.util.ArrayList;

public class java__VariableDeclarationExpression extends AbstractVariablesContainer, Expression {






    private java__Modifier java__modifier;




    private java__Modifier java__modifier;




    private List<java__Annotation> java__annotations;


    public java__VariableDeclarationExpression(
    ) {
        super(
        );
        this.java__annotations = new ArrayList<>();
    }

    public java__VariableDeclarationExpression(
        ArrayList<java__Annotation> java__annotations    ) {
        this.java__annotations = java__annotations;
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
    public List<java__Annotation> getJava__annotations() {
        return java__annotations;
    }

    public void addJava__annotation(Java__annotation java__annotation) {
        this.java__annotations.add(java__annotation);
    }

}