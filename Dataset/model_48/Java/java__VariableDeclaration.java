





import java.util.List;
import java.util.ArrayList;

public class java__VariableDeclaration extends NamedElement {

    private int extraArrayDimensions;





    private java__Expression java__expression;


    public java__VariableDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
    }


    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public java__Expression getJava__expression() {
        return java__expression;
    }

    public void setJava__expression(java__Expression java__expression) {
        this.java__expression = java__expression;
    }

}