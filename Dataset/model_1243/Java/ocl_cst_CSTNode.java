





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CSTNode  {

    private int endOffset;
    private int startOffset;



    public ocl_cst_CSTNode(
        int endOffset,        int startOffset    ) {
        this.endOffset = endOffset;
        this.startOffset = startOffset;
    }


    public int getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(int endOffset) {
        this.endOffset = endOffset;
    }
    public int getStartoffset() {
        return startOffset;
    }

    public void setStartoffset(int startOffset) {
        this.startOffset = startOffset;
    }


}