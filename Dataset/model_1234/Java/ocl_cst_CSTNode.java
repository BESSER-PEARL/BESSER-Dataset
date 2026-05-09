





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CSTNode  {

    private String endToken;
    private int endOffset;
    private String ast;
    private int startOffset;
    private String startToken;



    public ocl_cst_CSTNode(
        String endToken,        int endOffset,        String ast,        int startOffset,        String startToken    ) {
        this.endToken = endToken;
        this.endOffset = endOffset;
        this.ast = ast;
        this.startOffset = startOffset;
        this.startToken = startToken;
    }


    public String getEndtoken() {
        return endToken;
    }

    public void setEndtoken(String endToken) {
        this.endToken = endToken;
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
    public int getStartoffset() {
        return startOffset;
    }

    public void setStartoffset(int startOffset) {
        this.startOffset = startOffset;
    }
    public String getStarttoken() {
        return startToken;
    }

    public void setStarttoken(String startToken) {
        this.startToken = startToken;
    }


}