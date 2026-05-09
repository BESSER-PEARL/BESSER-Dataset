





import java.util.List;
import java.util.ArrayList;

public class gastm_SourceLocation extends GASTMSourceObject {

    private int endLine;
    private int endColumn;
    private int startColumn;
    private int startLine;



    public gastm_SourceLocation(
        int endLine,        int endColumn,        int startColumn,        int startLine    ) {
        super(
        );
        this.endLine = endLine;
        this.endColumn = endColumn;
        this.startColumn = startColumn;
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