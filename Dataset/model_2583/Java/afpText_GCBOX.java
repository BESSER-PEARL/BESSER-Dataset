





import java.util.List;
import java.util.ArrayList;

public class afpText_GCBOX extends triplet {

    private String VAXIS;
    private String YPOS1;
    private String HAXIS;
    private String RES;
    private String XPOS1;



    public afpText_GCBOX(
        String VAXIS,        String YPOS1,        String HAXIS,        String RES,        String XPOS1    ) {
        super(
        );
        this.VAXIS = VAXIS;
        this.YPOS1 = YPOS1;
        this.HAXIS = HAXIS;
        this.RES = RES;
        this.XPOS1 = XPOS1;
    }


    public String getVaxis() {
        return VAXIS;
    }

    public void setVaxis(String VAXIS) {
        this.VAXIS = VAXIS;
    }
    public String getYpos1() {
        return YPOS1;
    }

    public void setYpos1(String YPOS1) {
        this.YPOS1 = YPOS1;
    }
    public String getHaxis() {
        return HAXIS;
    }

    public void setHaxis(String HAXIS) {
        this.HAXIS = HAXIS;
    }
    public String getRes() {
        return RES;
    }

    public void setRes(String RES) {
        this.RES = RES;
    }
    public String getXpos1() {
        return XPOS1;
    }

    public void setXpos1(String XPOS1) {
        this.XPOS1 = XPOS1;
    }


}