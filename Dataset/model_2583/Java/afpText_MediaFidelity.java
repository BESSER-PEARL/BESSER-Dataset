





import java.util.List;
import java.util.ArrayList;

public class afpText_MediaFidelity extends triplet {

    private String StpMedEx;
    private String Reserved;



    public afpText_MediaFidelity(
        String StpMedEx,        String Reserved    ) {
        super(
        );
        this.StpMedEx = StpMedEx;
        this.Reserved = Reserved;
    }


    public String getStpmedex() {
        return StpMedEx;
    }

    public void setStpmedex(String StpMedEx) {
        this.StpMedEx = StpMedEx;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }


}