





import java.util.List;
import java.util.ArrayList;

public class mMDSL_FillColor  {

    private String color;
    private String hexcolor;





    private mMDSL_Text mmdsl_text;




    private mMDSL_SymbolStyle mmdsl_symbolstyle;


    public mMDSL_FillColor(
        String color,        String hexcolor    ) {
        this.color = color;
        this.hexcolor = hexcolor;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getHexcolor() {
        return hexcolor;
    }

    public void setHexcolor(String hexcolor) {
        this.hexcolor = hexcolor;
    }

    public mMDSL_Text getMmdsl_text() {
        return mmdsl_text;
    }

    public void setMmdsl_text(mMDSL_Text mmdsl_text) {
        this.mmdsl_text = mmdsl_text;
    }
    public mMDSL_SymbolStyle getMmdsl_symbolstyle() {
        return mmdsl_symbolstyle;
    }

    public void setMmdsl_symbolstyle(mMDSL_SymbolStyle mmdsl_symbolstyle) {
        this.mmdsl_symbolstyle = mmdsl_symbolstyle;
    }

}