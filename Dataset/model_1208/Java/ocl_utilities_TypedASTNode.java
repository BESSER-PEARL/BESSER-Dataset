





import java.util.List;
import java.util.ArrayList;

public class ocl_utilities_TypedASTNode extends ASTNode {

    private int typeStartPosition;
    private int typeEndPosition;



    public ocl_utilities_TypedASTNode(
        int typeStartPosition,        int typeEndPosition    ) {
        super(
        );
        this.typeStartPosition = typeStartPosition;
        this.typeEndPosition = typeEndPosition;
    }


    public int getTypestartposition() {
        return typeStartPosition;
    }

    public void setTypestartposition(int typeStartPosition) {
        this.typeStartPosition = typeStartPosition;
    }
    public int getTypeendposition() {
        return typeEndPosition;
    }

    public void setTypeendposition(int typeEndPosition) {
        this.typeEndPosition = typeEndPosition;
    }


}