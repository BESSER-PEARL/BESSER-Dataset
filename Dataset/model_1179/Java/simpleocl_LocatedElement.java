





import java.util.List;
import java.util.ArrayList;

public class simpleocl_LocatedElement  {

    private String column;
    private String charEnd;
    private String line;
    private String charStart;



    public simpleocl_LocatedElement(
        String column,        String charEnd,        String line,        String charStart    ) {
        this.column = column;
        this.charEnd = charEnd;
        this.line = line;
        this.charStart = charStart;
    }


    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }
    public String getCharend() {
        return charEnd;
    }

    public void setCharend(String charEnd) {
        this.charEnd = charEnd;
    }
    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
    }
    public String getCharstart() {
        return charStart;
    }

    public void setCharstart(String charStart) {
        this.charStart = charStart;
    }


}