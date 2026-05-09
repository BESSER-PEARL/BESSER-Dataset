





import java.util.List;
import java.util.ArrayList;

public class gastm_SourceLocation extends GASTMSourceObject {

    private int endColumn;
    private int startLine;
    private int endLine;
    private int startColumn;



    public gastm_SourceLocation(
        int endColumn,        int startLine,        int endLine,        int startColumn    ) {
        super(
        );
        this.endColumn = endColumn;
        this.startLine = startLine;
        this.endLine = endLine;
        this.startColumn = startColumn;
    }


    public int getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(int endColumn) {
        this.endColumn = endColumn;
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
    public int getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(int startColumn) {
        this.startColumn = startColumn;
    }


}