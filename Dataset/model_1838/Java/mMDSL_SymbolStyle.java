





import java.util.List;
import java.util.ArrayList;

public class mMDSL_SymbolStyle  {

    private String fontsize;
    private String strokewidth;
    private String name;





    private mMDSL_Method mmdsl_method;




    private List<mMDSL_InsertEmbedCode> mmdsl_insertembedcodes;


    public mMDSL_SymbolStyle(
        String fontsize,        String strokewidth,        String name    ) {
        this.fontsize = fontsize;
        this.strokewidth = strokewidth;
        this.name = name;
        this.mmdsl_insertembedcodes = new ArrayList<>();
    }

    public mMDSL_SymbolStyle(
        String fontsize,        String strokewidth,        String name        ArrayList<mMDSL_InsertEmbedCode> mmdsl_insertembedcodes    ) {
        this.fontsize = fontsize;
        this.strokewidth = strokewidth;
        this.name = name;
        this.mmdsl_insertembedcodes = mmdsl_insertembedcodes;
    }

    public String getFontsize() {
        return fontsize;
    }

    public void setFontsize(String fontsize) {
        this.fontsize = fontsize;
    }
    public String getStrokewidth() {
        return strokewidth;
    }

    public void setStrokewidth(String strokewidth) {
        this.strokewidth = strokewidth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_Method getMmdsl_method() {
        return mmdsl_method;
    }

    public void setMmdsl_method(mMDSL_Method mmdsl_method) {
        this.mmdsl_method = mmdsl_method;
    }
    public List<mMDSL_InsertEmbedCode> getMmdsl_insertembedcodes() {
        return mmdsl_insertembedcodes;
    }

    public void addMmdsl_insertembedcode(Mmdsl_insertembedcode mmdsl_insertembedcode) {
        this.mmdsl_insertembedcodes.add(mmdsl_insertembedcode);
    }

}