





import java.util.List;
import java.util.ArrayList;

public class platoon_Constraints  {

    private int lbound;
    private int ubound;



    public platoon_Constraints(
        int lbound,        int ubound    ) {
        this.lbound = lbound;
        this.ubound = ubound;
    }


    public int getLbound() {
        return lbound;
    }

    public void setLbound(int lbound) {
        this.lbound = lbound;
    }
    public int getUbound() {
        return ubound;
    }

    public void setUbound(int ubound) {
        this.ubound = ubound;
    }


}