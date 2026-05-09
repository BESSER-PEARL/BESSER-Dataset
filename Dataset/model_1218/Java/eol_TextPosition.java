





import java.util.List;
import java.util.ArrayList;

public class eol_TextPosition  {

    private int column;
    private int line;





    private eol_TextRegion eol_textregion;




    private eol_TextRegion eol_textregion;


    public eol_TextPosition(
        int column,        int line    ) {
        this.column = column;
        this.line = line;
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

    public eol_TextRegion getEol_textregion() {
        return eol_textregion;
    }

    public void setEol_textregion(eol_TextRegion eol_textregion) {
        this.eol_textregion = eol_textregion;
    }
    public eol_TextRegion getEol_textregion() {
        return eol_textregion;
    }

    public void setEol_textregion(eol_TextRegion eol_textregion) {
        this.eol_textregion = eol_textregion;
    }

}