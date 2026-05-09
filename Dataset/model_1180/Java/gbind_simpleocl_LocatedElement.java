





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_LocatedElement  {

    private String column;
    private String line;
    private String charEnd;
    private String charStart;



    public gbind_simpleocl_LocatedElement(
        String column,        String line,        String charEnd,        String charStart    ) {
        this.column = column;
        this.line = line;
        this.charEnd = charEnd;
        this.charStart = charStart;
    }


    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }
    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
    }
    public String getCharend() {
        return charEnd;
    }

    public void setCharend(String charEnd) {
        this.charEnd = charEnd;
    }
    public String getCharstart() {
        return charStart;
    }

    public void setCharstart(String charStart) {
        this.charStart = charStart;
    }


}