





import java.util.List;
import java.util.ArrayList;

public class eol_EolElement  {

    private int column;
    private int line;
    private String uri;





    private eol_EolElement eol_eolelement;


    public eol_EolElement(
        int column,        int line,        String uri    ) {
        this.column = column;
        this.line = line;
        this.uri = uri;
    }


    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public eol_EolElement getEol_eolelement() {
        return eol_eolelement;
    }

    public void setEol_eolelement(eol_EolElement eol_eolelement) {
        this.eol_eolelement = eol_eolelement;
    }

}