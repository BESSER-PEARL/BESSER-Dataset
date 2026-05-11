





import java.util.List;
import java.util.ArrayList;

public class afpText_TileTOCRG  {

    private String XOFFSET;
    private String DATAPOS;
    private String TVSIZE;
    private String THSIZE;
    private String RELRES;
    private String YOFFSET;
    private String COMPR;



    public afpText_TileTOCRG(
        String XOFFSET,        String DATAPOS,        String TVSIZE,        String THSIZE,        String RELRES,        String YOFFSET,        String COMPR    ) {
        this.XOFFSET = XOFFSET;
        this.DATAPOS = DATAPOS;
        this.TVSIZE = TVSIZE;
        this.THSIZE = THSIZE;
        this.RELRES = RELRES;
        this.YOFFSET = YOFFSET;
        this.COMPR = COMPR;
    }


    public String getXoffset() {
        return XOFFSET;
    }

    public void setXoffset(String XOFFSET) {
        this.XOFFSET = XOFFSET;
    }
    public String getDatapos() {
        return DATAPOS;
    }

    public void setDatapos(String DATAPOS) {
        this.DATAPOS = DATAPOS;
    }
    public String getTvsize() {
        return TVSIZE;
    }

    public void setTvsize(String TVSIZE) {
        this.TVSIZE = TVSIZE;
    }
    public String getThsize() {
        return THSIZE;
    }

    public void setThsize(String THSIZE) {
        this.THSIZE = THSIZE;
    }
    public String getRelres() {
        return RELRES;
    }

    public void setRelres(String RELRES) {
        this.RELRES = RELRES;
    }
    public String getYoffset() {
        return YOFFSET;
    }

    public void setYoffset(String YOFFSET) {
        this.YOFFSET = YOFFSET;
    }
    public String getCompr() {
        return COMPR;
    }

    public void setCompr(String COMPR) {
        this.COMPR = COMPR;
    }


}