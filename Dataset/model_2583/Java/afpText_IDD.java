





import java.util.List;
import java.util.ArrayList;

public class afpText_IDD extends structuredField {

    private String UNITBASE;
    private String XRESOL;
    private String YRESOL;
    private String YSIZE;
    private String XSIZE;



    public afpText_IDD(
        String UNITBASE,        String XRESOL,        String YRESOL,        String YSIZE,        String XSIZE    ) {
        super(
        );
        this.UNITBASE = UNITBASE;
        this.XRESOL = XRESOL;
        this.YRESOL = YRESOL;
        this.YSIZE = YSIZE;
        this.XSIZE = XSIZE;
    }


    public String getUnitbase() {
        return UNITBASE;
    }

    public void setUnitbase(String UNITBASE) {
        this.UNITBASE = UNITBASE;
    }
    public String getXresol() {
        return XRESOL;
    }

    public void setXresol(String XRESOL) {
        this.XRESOL = XRESOL;
    }
    public String getYresol() {
        return YRESOL;
    }

    public void setYresol(String YRESOL) {
        this.YRESOL = YRESOL;
    }
    public String getYsize() {
        return YSIZE;
    }

    public void setYsize(String YSIZE) {
        this.YSIZE = YSIZE;
    }
    public String getXsize() {
        return XSIZE;
    }

    public void setXsize(String XSIZE) {
        this.XSIZE = XSIZE;
    }


}