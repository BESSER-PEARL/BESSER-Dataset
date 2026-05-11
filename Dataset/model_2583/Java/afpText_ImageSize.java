





import java.util.List;
import java.util.ArrayList;

public class afpText_ImageSize extends triplet {

    private String VRESOL;
    private String VSIZE;
    private String UNITBASE;
    private String HRESOL;
    private String HSIZE;



    public afpText_ImageSize(
        String VRESOL,        String VSIZE,        String UNITBASE,        String HRESOL,        String HSIZE    ) {
        super(
        );
        this.VRESOL = VRESOL;
        this.VSIZE = VSIZE;
        this.UNITBASE = UNITBASE;
        this.HRESOL = HRESOL;
        this.HSIZE = HSIZE;
    }


    public String getVresol() {
        return VRESOL;
    }

    public void setVresol(String VRESOL) {
        this.VRESOL = VRESOL;
    }
    public String getVsize() {
        return VSIZE;
    }

    public void setVsize(String VSIZE) {
        this.VSIZE = VSIZE;
    }
    public String getUnitbase() {
        return UNITBASE;
    }

    public void setUnitbase(String UNITBASE) {
        this.UNITBASE = UNITBASE;
    }
    public String getHresol() {
        return HRESOL;
    }

    public void setHresol(String HRESOL) {
        this.HRESOL = HRESOL;
    }
    public String getHsize() {
        return HSIZE;
    }

    public void setHsize(String HSIZE) {
        this.HSIZE = HSIZE;
    }


}