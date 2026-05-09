





import java.util.List;
import java.util.ArrayList;

public class gastm_SourceLocation extends GASTMSourceObject {

    private int endLine;
    private int startLine;
    private int endColumn;
    private int startColumn;





    private SourceFile sourcefile;


    public gastm_SourceLocation(
        int endLine,        int startLine,        int endColumn,        int startColumn    ) {
        super(
        );
        this.endLine = endLine;
        this.startLine = startLine;
        this.endColumn = endColumn;
        this.startColumn = startColumn;
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
    public int getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(int startColumn) {
        this.startColumn = startColumn;
    }

    public SourceFile getSourcefile() {
        return sourcefile;
    }

    public void setSourcefile(SourceFile sourcefile) {
        this.sourcefile = sourcefile;
    }

}