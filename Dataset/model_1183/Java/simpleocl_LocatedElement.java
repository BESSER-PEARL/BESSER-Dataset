





import java.util.List;
import java.util.ArrayList;

public class simpleocl_LocatedElement  {

    private String line;
    private String charStart;
    private String charEnd;
    private String column;



    public simpleocl_LocatedElement(
        String line,        String charStart,        String charEnd,        String column    ) {
        this.line = line;
        this.charStart = charStart;
        this.charEnd = charEnd;
        this.column = column;
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


}