





import java.util.List;
import java.util.ArrayList;

public class afpText_GBOX extends triplet {

    private String VAXIS;
    private String XPOS1;
    private String YPOS1;
    private String RES;
    private String YPOS0;
    private String XPOS0;
    private String HAXIS;



    public afpText_GBOX(
        String VAXIS,        String XPOS1,        String YPOS1,        String RES,        String YPOS0,        String XPOS0,        String HAXIS    ) {
        super(
        );
        this.VAXIS = VAXIS;
        this.XPOS1 = XPOS1;
        this.YPOS1 = YPOS1;
        this.RES = RES;
        this.YPOS0 = YPOS0;
        this.XPOS0 = XPOS0;
        this.HAXIS = HAXIS;
    }


    public String getVaxis() {
        return VAXIS;
    }

    public void setVaxis(String VAXIS) {
        this.VAXIS = VAXIS;
    }
    public String getXpos1() {
        return XPOS1;
    }

    public void setXpos1(String XPOS1) {
        this.XPOS1 = XPOS1;
    }
    public String getYpos1() {
        return YPOS1;
    }

    public void setYpos1(String YPOS1) {
        this.YPOS1 = YPOS1;
    }
    public String getRes() {
        return RES;
    }

    public void setRes(String RES) {
        this.RES = RES;
    }
    public String getYpos0() {
        return YPOS0;
    }

    public void setYpos0(String YPOS0) {
        this.YPOS0 = YPOS0;
    }
    public String getXpos0() {
        return XPOS0;
    }

    public void setXpos0(String XPOS0) {
        this.XPOS0 = XPOS0;
    }
    public String getHaxis() {
        return HAXIS;
    }

    public void setHaxis(String HAXIS) {
        this.HAXIS = HAXIS;
    }


}