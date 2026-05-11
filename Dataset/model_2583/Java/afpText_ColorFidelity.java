





import java.util.List;
import java.util.ArrayList;

public class afpText_ColorFidelity extends triplet {

    private String ColSub;
    private String RepCoEx;
    private String StpCoEx;



    public afpText_ColorFidelity(
        String ColSub,        String RepCoEx,        String StpCoEx    ) {
        super(
        );
        this.ColSub = ColSub;
        this.RepCoEx = RepCoEx;
        this.StpCoEx = StpCoEx;
    }


    public String getColsub() {
        return ColSub;
    }

    public void setColsub(String ColSub) {
        this.ColSub = ColSub;
    }
    public String getRepcoex() {
        return RepCoEx;
    }

    public void setRepcoex(String RepCoEx) {
        this.RepCoEx = RepCoEx;
    }
    public String getStpcoex() {
        return StpCoEx;
    }

    public void setStpcoex(String StpCoEx) {
        this.StpCoEx = StpCoEx;
    }


}