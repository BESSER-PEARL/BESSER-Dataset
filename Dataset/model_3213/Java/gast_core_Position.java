





import java.util.List;
import java.util.ArrayList;

public class gast_core_Position  {

    private int endLine;
    private int startLine;
    private int endColumn;
    private int startColumn;





    private File file;




    private SourceEntity sourceentity;




    private File file;


    public gast_core_Position(
        int endLine,        int startLine,        int endColumn,        int startColumn    ) {
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

    public File getFile() {
        return file;
    }

    public void setFile(File file) {
        this.file = file;
    }
    public SourceEntity getSourceentity() {
        return sourceentity;
    }

    public void setSourceentity(SourceEntity sourceentity) {
        this.sourceentity = sourceentity;
    }
    public File getFile() {
        return file;
    }

    public void setFile(File file) {
        this.file = file;
    }

}