





import java.util.List;
import java.util.ArrayList;

public class ast_EJElement  {

    private int startColumn;
    private String startOffset;
    private int endLine;
    private int startLine;
    private int endColumn;
    private String endOffset;



    public ast_EJElement(
        int startColumn,        String startOffset,        int endLine,        int startLine,        int endColumn,        String endOffset    ) {
        this.startColumn = startColumn;
        this.startOffset = startOffset;
        this.endLine = endLine;
        this.startLine = startLine;
        this.endColumn = endColumn;
        this.endOffset = endOffset;
    }


    public int getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(int startColumn) {
        this.startColumn = startColumn;
    }
    public String getStartoffset() {
        return startOffset;
    }

    public void setStartoffset(String startOffset) {
        this.startOffset = startOffset;
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
    public int getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(int endColumn) {
        this.endColumn = endColumn;
    }
    public String getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(String endOffset) {
        this.endOffset = endOffset;
    }


}