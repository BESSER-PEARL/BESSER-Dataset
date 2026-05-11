





import java.util.List;
import java.util.ArrayList;

public class afpText_WindowSpecification extends triplet {

    private String IMGXYRES;
    private String YTWIND;
    private String UBASE;
    private String RES3;
    private String CFORMAT;
    private String YBWIND;
    private String XLWIND;
    private String XRWIND;
    private String XRESOL;
    private String FLAGS;
    private String YRESOL;



    public afpText_WindowSpecification(
        String IMGXYRES,        String YTWIND,        String UBASE,        String RES3,        String CFORMAT,        String YBWIND,        String XLWIND,        String XRWIND,        String XRESOL,        String FLAGS,        String YRESOL    ) {
        super(
        );
        this.IMGXYRES = IMGXYRES;
        this.YTWIND = YTWIND;
        this.UBASE = UBASE;
        this.RES3 = RES3;
        this.CFORMAT = CFORMAT;
        this.YBWIND = YBWIND;
        this.XLWIND = XLWIND;
        this.XRWIND = XRWIND;
        this.XRESOL = XRESOL;
        this.FLAGS = FLAGS;
        this.YRESOL = YRESOL;
    }


    public String getImgxyres() {
        return IMGXYRES;
    }

    public void setImgxyres(String IMGXYRES) {
        this.IMGXYRES = IMGXYRES;
    }
    public String getYtwind() {
        return YTWIND;
    }

    public void setYtwind(String YTWIND) {
        this.YTWIND = YTWIND;
    }
    public String getUbase() {
        return UBASE;
    }

    public void setUbase(String UBASE) {
        this.UBASE = UBASE;
    }
    public String getRes3() {
        return RES3;
    }

    public void setRes3(String RES3) {
        this.RES3 = RES3;
    }
    public String getCformat() {
        return CFORMAT;
    }

    public void setCformat(String CFORMAT) {
        this.CFORMAT = CFORMAT;
    }
    public String getYbwind() {
        return YBWIND;
    }

    public void setYbwind(String YBWIND) {
        this.YBWIND = YBWIND;
    }
    public String getXlwind() {
        return XLWIND;
    }

    public void setXlwind(String XLWIND) {
        this.XLWIND = XLWIND;
    }
    public String getXrwind() {
        return XRWIND;
    }

    public void setXrwind(String XRWIND) {
        this.XRWIND = XRWIND;
    }
    public String getXresol() {
        return XRESOL;
    }

    public void setXresol(String XRESOL) {
        this.XRESOL = XRESOL;
    }
    public String getFlags() {
        return FLAGS;
    }

    public void setFlags(String FLAGS) {
        this.FLAGS = FLAGS;
    }
    public String getYresol() {
        return YRESOL;
    }

    public void setYresol(String YRESOL) {
        this.YRESOL = YRESOL;
    }


}