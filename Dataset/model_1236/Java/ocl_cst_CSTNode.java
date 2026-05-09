





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CSTNode  {

    private String startToken;
    private int endOffset;
    private String endToken;
    private int startOffset;
    private String ast;



    public ocl_cst_CSTNode(
        String startToken,        int endOffset,        String endToken,        int startOffset,        String ast    ) {
        this.startToken = startToken;
        this.endOffset = endOffset;
        this.endToken = endToken;
        this.startOffset = startOffset;
        this.ast = ast;
    }


    public String getStarttoken() {
        return startToken;
    }

    public void setStarttoken(String startToken) {
        this.startToken = startToken;
    }
    public int getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(int endOffset) {
        this.endOffset = endOffset;
    }
    public String getEndtoken() {
        return endToken;
    }

    public void setEndtoken(String endToken) {
        this.endToken = endToken;
    }
    public int getStartoffset() {
        return startOffset;
    }

    public void setStartoffset(int startOffset) {
        this.startOffset = startOffset;
    }
    public String getAst() {
        return ast;
    }

    public void setAst(String ast) {
        this.ast = ast;
    }


}