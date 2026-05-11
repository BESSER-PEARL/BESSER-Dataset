





import java.util.List;
import java.util.ArrayList;

public class afpText_CMRFidelity extends triplet {

    private String StpCMREx;
    private String RepCMREx;



    public afpText_CMRFidelity(
        String StpCMREx,        String RepCMREx    ) {
        super(
        );
        this.StpCMREx = StpCMREx;
        this.RepCMREx = RepCMREx;
    }


    public String getStpcmrex() {
        return StpCMREx;
    }

    public void setStpcmrex(String StpCMREx) {
        this.StpCMREx = StpCMREx;
    }
    public String getRepcmrex() {
        return RepCMREx;
    }

    public void setRepcmrex(String RepCMREx) {
        this.RepCMREx = RepCMREx;
    }


}