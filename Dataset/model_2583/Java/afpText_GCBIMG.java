





import java.util.List;
import java.util.ArrayList;

public class afpText_GCBIMG extends triplet {

    private String WIDTH;
    private String HEIGHT;
    private String FORMAT;
    private String RES;



    public afpText_GCBIMG(
        String WIDTH,        String HEIGHT,        String FORMAT,        String RES    ) {
        super(
        );
        this.WIDTH = WIDTH;
        this.HEIGHT = HEIGHT;
        this.FORMAT = FORMAT;
        this.RES = RES;
    }


    public String getWidth() {
        return WIDTH;
    }

    public void setWidth(String WIDTH) {
        this.WIDTH = WIDTH;
    }
    public String getHeight() {
        return HEIGHT;
    }

    public void setHeight(String HEIGHT) {
        this.HEIGHT = HEIGHT;
    }
    public String getFormat() {
        return FORMAT;
    }

    public void setFormat(String FORMAT) {
        this.FORMAT = FORMAT;
    }
    public String getRes() {
        return RES;
    }

    public void setRes(String RES) {
        this.RES = RES;
    }


}