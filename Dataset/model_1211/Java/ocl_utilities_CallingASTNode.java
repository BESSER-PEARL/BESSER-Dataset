





import java.util.List;
import java.util.ArrayList;

public class ocl_utilities_CallingASTNode extends ASTNode {

    private int propertyEndPosition;
    private int propertyStartPosition;



    public ocl_utilities_CallingASTNode(
        int propertyEndPosition,        int propertyStartPosition    ) {
        super(
        );
        this.propertyEndPosition = propertyEndPosition;
        this.propertyStartPosition = propertyStartPosition;
    }


    public int getPropertyendposition() {
        return propertyEndPosition;
    }

    public void setPropertyendposition(int propertyEndPosition) {
        this.propertyEndPosition = propertyEndPosition;
    }
    public int getPropertystartposition() {
        return propertyStartPosition;
    }

    public void setPropertystartposition(int propertyStartPosition) {
        this.propertyStartPosition = propertyStartPosition;
    }


}