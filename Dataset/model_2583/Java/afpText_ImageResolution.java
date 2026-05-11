





import java.util.List;
import java.util.ArrayList;

public class afpText_ImageResolution extends triplet {

    private String YBase;
    private String XBase;
    private String XResol;
    private String YResol;



    public afpText_ImageResolution(
        String YBase,        String XBase,        String XResol,        String YResol    ) {
        super(
        );
        this.YBase = YBase;
        this.XBase = XBase;
        this.XResol = XResol;
        this.YResol = YResol;
    }


    public String getYbase() {
        return YBase;
    }

    public void setYbase(String YBase) {
        this.YBase = YBase;
    }
    public String getXbase() {
        return XBase;
    }

    public void setXbase(String XBase) {
        this.XBase = XBase;
    }
    public String getXresol() {
        return XResol;
    }

    public void setXresol(String XResol) {
        this.XResol = XResol;
    }
    public String getYresol() {
        return YResol;
    }

    public void setYresol(String YResol) {
        this.YResol = YResol;
    }


}