





import java.util.List;
import java.util.ArrayList;

public class ocl_utilities_ASTNode  {

    private int startPosition;
    private int endPosition;



    public ocl_utilities_ASTNode(
        int startPosition,        int endPosition    ) {
        this.startPosition = startPosition;
        this.endPosition = endPosition;
    }


    public int getStartposition() {
        return startPosition;
    }

    public void setStartposition(int startPosition) {
        this.startPosition = startPosition;
    }
    public int getEndposition() {
        return endPosition;
    }

    public void setEndposition(int endPosition) {
        this.endPosition = endPosition;
    }


}