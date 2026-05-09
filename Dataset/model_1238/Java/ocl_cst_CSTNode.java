





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CSTNode  {

    private String ast;
    private int endOffset;
    private String startToken;
    private int startOffset;
    private String endToken;



    public ocl_cst_CSTNode(
        String ast,        int endOffset,        String startToken,        int startOffset,        String endToken    ) {
        this.ast = ast;
        this.endOffset = endOffset;
        this.startToken = startToken;
        this.startOffset = startOffset;
        this.endToken = endToken;
    }


    public String getAst() {
        return ast;
    }

    public void setAst(String ast) {
        this.ast = ast;
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