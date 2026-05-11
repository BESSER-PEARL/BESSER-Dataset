





import java.util.List;
import java.util.ArrayList;

public class afpText_FinishingFidelity extends triplet {

    private String RepFinEx;
    private String StpFinEx;



    public afpText_FinishingFidelity(
        String RepFinEx,        String StpFinEx    ) {
        super(
        );
        this.RepFinEx = RepFinEx;
        this.StpFinEx = StpFinEx;
    }


    public String getRepfinex() {
        return RepFinEx;
    }

    public void setRepfinex(String RepFinEx) {
        this.RepFinEx = RepFinEx;
    }
    public String getStpfinex() {
        return StpFinEx;
    }

    public void setStpfinex(String StpFinEx) {
        this.StpFinEx = StpFinEx;
    }


}