





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_SourceLocation extends GASTMSourceObject {

    private int startColumn;
    private int startLine;
    private int endColumn;
    private int endLine;



    public astm_gastm_SourceLocation(
        int startColumn,        int startLine,        int endColumn,        int endLine    ) {
        super(
        );
        this.startColumn = startColumn;
        this.startLine = startLine;
        this.endColumn = endColumn;
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


}