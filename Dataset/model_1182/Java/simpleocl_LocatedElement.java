





import java.util.List;
import java.util.ArrayList;

public class simpleocl_LocatedElement  {

    private String charEnd;
    private String column;
    private String charStart;
    private String line;



    public simpleocl_LocatedElement(
        String charEnd,        String column,        String charStart,        String line    ) {
        this.charEnd = charEnd;
        this.column = column;
        this.charStart = charStart;
        this.line = line;
    }


    public String getCharend() {
        return charEnd;
    }

    public void setCharend(String charEnd) {
        this.charEnd = charEnd;
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
    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
    }


}