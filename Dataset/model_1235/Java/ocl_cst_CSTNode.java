





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CSTNode  {

    private int endOffset;
    private String startToken;
    private String ast;
    private int startOffset;
    private String endToken;



    public ocl_cst_CSTNode(
        int endOffset,        String startToken,        String ast,        int startOffset,        String endToken    ) {
        this.endOffset = endOffset;
        this.startToken = startToken;
        this.ast = ast;
        this.startOffset = startOffset;
        this.endToken = endToken;
    }


    public int getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(int endOffset) {
        this.endOffset = endOffset;
    }
    public String getStarttoken() {
        return startToken;
    }

    public void setStarttoken(String startToken) {
        this.startToken = startToken;
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
    public String getEndtoken() {
        return endToken;
    }

    public void setEndtoken(String endToken) {
        this.endToken = endToken;
    }


}