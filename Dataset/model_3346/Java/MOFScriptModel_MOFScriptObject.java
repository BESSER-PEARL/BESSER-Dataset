





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptObject  {

    private int line;
    private int column;





    private List<MOFScriptModel_MOFScriptComment> mofscriptmodel_mofscriptcomments;


    public MOFScriptModel_MOFScriptObject(
        int line,        int column    ) {
        this.line = line;
        this.column = column;
        this.mofscriptmodel_mofscriptcomments = new ArrayList<>();
    }

    public MOFScriptModel_MOFScriptObject(
        int line,        int column        ArrayList<MOFScriptModel_MOFScriptComment> mofscriptmodel_mofscriptcomments    ) {
        this.line = line;
        this.column = column;
        this.mofscriptmodel_mofscriptcomments = mofscriptmodel_mofscriptcomments;
    }

    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }
    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }

    public List<MOFScriptModel_MOFScriptComment> getMofscriptmodel_mofscriptcomments() {
        return mofscriptmodel_mofscriptcomments;
    }

    public void addMofscriptmodel_mofscriptcomment(Mofscriptmodel_mofscriptcomment mofscriptmodel_mofscriptcomment) {
        this.mofscriptmodel_mofscriptcomments.add(mofscriptmodel_mofscriptcomment);
    }

}