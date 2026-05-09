





import java.util.List;
import java.util.ArrayList;

public class ocl_utilities_TypedASTNode extends ASTNode {

    private int typeEndPosition;
    private int typeStartPosition;



    public ocl_utilities_TypedASTNode(
        int typeEndPosition,        int typeStartPosition    ) {
        super(
        );
        this.typeEndPosition = typeEndPosition;
        this.typeStartPosition = typeStartPosition;
    }


    public int getTypeendposition() {
        return typeEndPosition;
    }

    public void setTypeendposition(int typeEndPosition) {
        this.typeEndPosition = typeEndPosition;
    }
    public int getTypestartposition() {
        return typeStartPosition;
    }

    public void setTypestartposition(int typeStartPosition) {
        this.typeStartPosition = typeStartPosition;
    }


}