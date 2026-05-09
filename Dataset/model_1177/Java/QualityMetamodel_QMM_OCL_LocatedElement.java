





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QMM_OCL_LocatedElement  {

    private String line;
    private String column;
    private String charStart;
    private String charEnd;



    public QualityMetamodel_QMM_OCL_LocatedElement(
        String line,        String column,        String charStart,        String charEnd    ) {
        this.line = line;
        this.column = column;
        this.charStart = charStart;
        this.charEnd = charEnd;
    }


    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
    }
    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }
    public String getCharstart() {
        return charStart;
    }

    public void setCharstart(String charStart) {
        this.charStart = charStart;
    }
    public String getCharend() {
        return charEnd;
    }

    public void setCharend(String charEnd) {
        this.charEnd = charEnd;
    }


}