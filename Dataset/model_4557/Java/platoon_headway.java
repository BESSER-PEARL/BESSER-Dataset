





import java.util.List;
import java.util.ArrayList;

public class platoon_headway extends Constraint {

    private int lowbound;
    private int upbound;



    public platoon_headway(
        int lowbound,        int upbound    ) {
        super(
        );
        this.lowbound = lowbound;
        this.upbound = upbound;
    }


    public int getLowbound() {
        return lowbound;
    }

    public void setLowbound(int lowbound) {
        this.lowbound = lowbound;
    }
    public int getUpbound() {
        return upbound;
    }

    public void setUpbound(int upbound) {
        this.upbound = upbound;
    }


}