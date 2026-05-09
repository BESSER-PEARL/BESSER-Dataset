





import java.util.List;
import java.util.ArrayList;

public class ast_EJElement  {

    private String startOffset;
    private int endColumn;
    private int startColumn;
    private String endOffset;
    private int endLine;
    private int startLine;



    public ast_EJElement(
        String startOffset,        int endColumn,        int startColumn,        String endOffset,        int endLine,        int startLine    ) {
        this.startOffset = startOffset;
        this.endColumn = endColumn;
        this.startColumn = startColumn;
        this.endOffset = endOffset;
        this.endLine = endLine;
        this.startLine = startLine;
    }


    public String getStartoffset() {
        return startOffset;
    }

    public void setStartoffset(String startOffset) {
        this.startOffset = startOffset;
    }
    public int getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(int endColumn) {
        this.endColumn = endColumn;
    }
    public int getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(int startColumn) {
        this.startColumn = startColumn;
    }
    public String getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(String endOffset) {
        this.endOffset = endOffset;
    }
    public int getEndline() {
        return endLine;
    }

    public void setEndline(int endLine) {
        this.endLine = endLine;
    }
    public int getStartline() {
        return startLine;
    }

    public void setStartline(int startLine) {
        this.startLine = startLine;
    }


}