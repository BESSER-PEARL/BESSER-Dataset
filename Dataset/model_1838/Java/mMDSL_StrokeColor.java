





import java.util.List;
import java.util.ArrayList;

public class mMDSL_StrokeColor  {

    private String hexcolor;
    private String color;





    private mMDSL_SymbolStyle mmdsl_symbolstyle;


    public mMDSL_StrokeColor(
        String hexcolor,        String color    ) {
        this.hexcolor = hexcolor;
        this.color = color;
    }


    public String getHexcolor() {
        return hexcolor;
    }

    public void setHexcolor(String hexcolor) {
        this.hexcolor = hexcolor;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public mMDSL_SymbolStyle getMmdsl_symbolstyle() {
        return mmdsl_symbolstyle;
    }

    public void setMmdsl_symbolstyle(mMDSL_SymbolStyle mmdsl_symbolstyle) {
        this.mmdsl_symbolstyle = mmdsl_symbolstyle;
    }

}