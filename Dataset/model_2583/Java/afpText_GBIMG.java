





import java.util.List;
import java.util.ArrayList;

public class afpText_GBIMG extends triplet {

    private String WIDTH;
    private String RES;
    private String YPOS;
    private String XPOS;
    private String FORMAT;
    private String HEIGHT;



    public afpText_GBIMG(
        String WIDTH,        String RES,        String YPOS,        String XPOS,        String FORMAT,        String HEIGHT    ) {
        super(
        );
        this.WIDTH = WIDTH;
        this.RES = RES;
        this.YPOS = YPOS;
        this.XPOS = XPOS;
        this.FORMAT = FORMAT;
        this.HEIGHT = HEIGHT;
    }


    public String getWidth() {
        return WIDTH;
    }

    public void setWidth(String WIDTH) {
        this.WIDTH = WIDTH;
    }
    public String getRes() {
        return RES;
    }

    public void setRes(String RES) {
        this.RES = RES;
    }
    public String getYpos() {
        return YPOS;
    }

    public void setYpos(String YPOS) {
        this.YPOS = YPOS;
    }
    public String getXpos() {
        return XPOS;
    }

    public void setXpos(String XPOS) {
        this.XPOS = XPOS;
    }
    public String getFormat() {
        return FORMAT;
    }

    public void setFormat(String FORMAT) {
        this.FORMAT = FORMAT;
    }
    public String getHeight() {
        return HEIGHT;
    }

    public void setHeight(String HEIGHT) {
        this.HEIGHT = HEIGHT;
    }


}