





import java.util.List;
import java.util.ArrayList;

public class afpText_BDD extends structuredField {

    private String XEXTENT;
    private String XUPUB;
    private String MOD;
    private String WENE;
    private String YEXTENT;
    private String COLOR;
    private String YUPUB;
    private String MODULEWIDTH;
    private String Reserved2;
    private String UBASE;
    private String ELEMENTHEIGHT;
    private String LID;
    private String TYPE;
    private String Reserved;
    private String MULT;



    public afpText_BDD(
        String XEXTENT,        String XUPUB,        String MOD,        String WENE,        String YEXTENT,        String COLOR,        String YUPUB,        String MODULEWIDTH,        String Reserved2,        String UBASE,        String ELEMENTHEIGHT,        String LID,        String TYPE,        String Reserved,        String MULT    ) {
        super(
        );
        this.XEXTENT = XEXTENT;
        this.XUPUB = XUPUB;
        this.MOD = MOD;
        this.WENE = WENE;
        this.YEXTENT = YEXTENT;
        this.COLOR = COLOR;
        this.YUPUB = YUPUB;
        this.MODULEWIDTH = MODULEWIDTH;
        this.Reserved2 = Reserved2;
        this.UBASE = UBASE;
        this.ELEMENTHEIGHT = ELEMENTHEIGHT;
        this.LID = LID;
        this.TYPE = TYPE;
        this.Reserved = Reserved;
        this.MULT = MULT;
    }


    public String getXextent() {
        return XEXTENT;
    }

    public void setXextent(String XEXTENT) {
        this.XEXTENT = XEXTENT;
    }
    public String getXupub() {
        return XUPUB;
    }

    public void setXupub(String XUPUB) {
        this.XUPUB = XUPUB;
    }
    public String getMod() {
        return MOD;
    }

    public void setMod(String MOD) {
        this.MOD = MOD;
    }
    public String getWene() {
        return WENE;
    }

    public void setWene(String WENE) {
        this.WENE = WENE;
    }
    public String getYextent() {
        return YEXTENT;
    }

    public void setYextent(String YEXTENT) {
        this.YEXTENT = YEXTENT;
    }
    public String getColor() {
        return COLOR;
    }

    public void setColor(String COLOR) {
        this.COLOR = COLOR;
    }
    public String getYupub() {
        return YUPUB;
    }

    public void setYupub(String YUPUB) {
        this.YUPUB = YUPUB;
    }
    public String getModulewidth() {
        return MODULEWIDTH;
    }

    public void setModulewidth(String MODULEWIDTH) {
        this.MODULEWIDTH = MODULEWIDTH;
    }
    public String getReserved2() {
        return Reserved2;
    }

    public void setReserved2(String Reserved2) {
        this.Reserved2 = Reserved2;
    }
    public String getUbase() {
        return UBASE;
    }

    public void setUbase(String UBASE) {
        this.UBASE = UBASE;
    }
    public String getElementheight() {
        return ELEMENTHEIGHT;
    }

    public void setElementheight(String ELEMENTHEIGHT) {
        this.ELEMENTHEIGHT = ELEMENTHEIGHT;
    }
    public String getLid() {
        return LID;
    }

    public void setLid(String LID) {
        this.LID = LID;
    }
    public String getType() {
        return TYPE;
    }

    public void setType(String TYPE) {
        this.TYPE = TYPE;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getMult() {
        return MULT;
    }

    public void setMult(String MULT) {
        this.MULT = MULT;
    }


}