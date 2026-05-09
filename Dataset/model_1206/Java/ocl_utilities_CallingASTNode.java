





import java.util.List;
import java.util.ArrayList;

public class ocl_utilities_CallingASTNode extends ASTNode {

    private int propertyStartPosition;
    private int propertyEndPosition;



    public ocl_utilities_CallingASTNode(
        int propertyStartPosition,        int propertyEndPosition    ) {
        super(
        );
        this.propertyStartPosition = propertyStartPosition;
        this.propertyEndPosition = propertyEndPosition;
    }


    public int getPropertystartposition() {
        return propertyStartPosition;
    }

    public void setPropertystartposition(int propertyStartPosition) {
        this.propertyStartPosition = propertyStartPosition;
    }
    public int getPropertyendposition() {
        return propertyEndPosition;
    }

    public void setPropertyendposition(int propertyEndPosition) {
        this.propertyEndPosition = propertyEndPosition;
    }


}