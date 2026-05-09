





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_SourceLocation extends GASTMSourceObject {

    private int startLine;
    private int endLine;
    private int startColumn;
    private int endColumn;



    public astm_gastm_SourceLocation(
        int startLine,        int endLine,        int startColumn,        int endColumn    ) {
        super(
        );
        this.startLine = startLine;
        this.endLine = endLine;
        this.startColumn = startColumn;
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
    public int getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(int endColumn) {
        this.endColumn = endColumn;
    }


}