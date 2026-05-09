





import java.util.List;
import java.util.ArrayList;

public class astm_SourceLocation extends GASTMSourceObject {

    private int endLine;
    private int endColumn;
    private int startLine;
    private int startColumn;





    private astm_SourceFile astm_sourcefile;


    public astm_SourceLocation(
        int endLine,        int endColumn,        int startLine,        int startColumn    ) {
        super(
        );
        this.endLine = endLine;
        this.endColumn = endColumn;
        this.startLine = startLine;
        this.startColumn = startColumn;
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
    public int getStartline() {
        return startLine;
    }

    public void setStartline(int startLine) {
        this.startLine = startLine;
    }
    public int getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(int startColumn) {
        this.startColumn = startColumn;
    }

    public astm_SourceFile getAstm_sourcefile() {
        return astm_sourcefile;
    }

    public void setAstm_sourcefile(astm_SourceFile astm_sourcefile) {
        this.astm_sourcefile = astm_sourcefile;
    }

}