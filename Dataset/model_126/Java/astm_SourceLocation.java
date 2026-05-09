





import java.util.List;
import java.util.ArrayList;

public class astm_SourceLocation extends GASTMSourceObject {

    private int endColumn;
    private int endLine;
    private int startColumn;
    private int startLine;



    public astm_SourceLocation(
        int endColumn,        int endLine,        int startColumn,        int startLine    ) {
        super(
        );
        this.endColumn = endColumn;
        this.endLine = endLine;
        this.startColumn = startColumn;
        this.startLine = startLine;
    }


    public int getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(int endColumn) {
        this.endColumn = endColumn;
    }
    public int getEndline() {
        return endLine;
    }

    public void setEndline(int endLine) {
        this.endLine = endLine;
    }
    public int getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(int startColumn) {
        this.startColumn = startColumn;
    }
    public int getStartline() {
        return startLine;
    }

    public void setStartline(int startLine) {
        this.startLine = startLine;
    }


}