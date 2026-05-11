





import java.util.List;
import java.util.ArrayList;

public class dg_Translate extends Transform {

    private String deltaY;
    private String deltaX;



    public dg_Translate(
        String deltaY,        String deltaX    ) {
        super(
        );
        this.deltaY = deltaY;
        this.deltaX = deltaX;
    }


    public String getDeltay() {
        return deltaY;
    }

    public void setDeltay(String deltaY) {
        this.deltaY = deltaY;
    }
    public String getDeltax() {
        return deltaX;
    }

    public void setDeltax(String deltaX) {
        this.deltaX = deltaX;
    }


}