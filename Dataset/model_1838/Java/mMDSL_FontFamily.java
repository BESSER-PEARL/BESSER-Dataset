





import java.util.List;
import java.util.ArrayList;

public class mMDSL_FontFamily  {

    private String fontstr;
    private String font;





    private mMDSL_Text mmdsl_text;




    private mMDSL_SymbolStyle mmdsl_symbolstyle;


    public mMDSL_FontFamily(
        String fontstr,        String font    ) {
        this.fontstr = fontstr;
        this.font = font;
    }


    public String getFontstr() {
        return fontstr;
    }

    public void setFontstr(String fontstr) {
        this.fontstr = fontstr;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
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