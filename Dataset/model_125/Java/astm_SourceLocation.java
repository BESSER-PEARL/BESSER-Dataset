





import java.util.List;
import java.util.ArrayList;

public class astm_SourceLocation extends GASTMSourceObject {

    private int startColumn;
    private int startLine;
    private int endLine;
    private int endColumn;



    public astm_SourceLocation(
        int startColumn,        int startLine,        int endLine,        int endColumn    ) {
        super(
        );
        this.startColumn = startColumn;
        this.startLine = startLine;
        this.endLine = endLine;
        this.endColumn = endColumn;
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
    public int getEndline() {
        return endLine;
    }

    public void setEndline(int endLine) {
        this.endLine = endLine;
    }
    public int getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(int endColumn) {
        this.endColumn = endColumn;
    }


}