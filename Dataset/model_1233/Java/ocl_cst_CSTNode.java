





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CSTNode  {

    private String startToken;
    private int startOffset;
    private int endOffset;
    private String ast;
    private String endToken;



    public ocl_cst_CSTNode(
        String startToken,        int startOffset,        int endOffset,        String ast,        String endToken    ) {
        this.startToken = startToken;
        this.startOffset = startOffset;
        this.endOffset = endOffset;
        this.ast = ast;
        this.endToken = endToken;
    }


    public String getStarttoken() {
        return startToken;
    }

    public void setStarttoken(String startToken) {
        this.startToken = startToken;
    }
    public int getStartoffset() {
        return startOffset;
    }

    public void setStartoffset(int startOffset) {
        this.startOffset = startOffset;
    }
    public int getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(int endOffset) {
        this.endOffset = endOffset;
    }
    public String getAst() {
        return ast;
    }

    public void setAst(String ast) {
        this.ast = ast;
    }
    public String getEndtoken() {
        return endToken;
    }

    public void setEndtoken(String endToken) {
        this.endToken = endToken;
    }


}