





import java.util.List;
import java.util.ArrayList;

public class afpText_GCHST extends triplet {

    private String XPOS;
    private String CP;
    private String YPOS;



    public afpText_GCHST(
        String XPOS,        String CP,        String YPOS    ) {
        super(
        );
        this.XPOS = XPOS;
        this.CP = CP;
        this.YPOS = YPOS;
    }


    public String getXpos() {
        return XPOS;
    }

    public void setXpos(String XPOS) {
        this.XPOS = XPOS;
    }
    public String getCp() {
        return CP;
    }

    public void setCp(String CP) {
        this.CP = CP;
    }
    public String getYpos() {
        return YPOS;
    }

    public void setYpos(String YPOS) {
        this.YPOS = YPOS;
    }


}