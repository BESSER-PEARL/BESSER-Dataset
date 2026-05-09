





import java.util.List;
import java.util.ArrayList;

public class cst_CSTNode  {

    private int endPosition;
    private int startPosition;



    public cst_CSTNode(
        int endPosition,        int startPosition    ) {
        this.endPosition = endPosition;
        this.startPosition = startPosition;
    }


    public int getEndposition() {
        return endPosition;
    }

    public void setEndposition(int endPosition) {
        this.endPosition = endPosition;
    }
    public int getStartposition() {
        return startPosition;
    }

    public void setStartposition(int startPosition) {
        this.startPosition = startPosition;
    }


}