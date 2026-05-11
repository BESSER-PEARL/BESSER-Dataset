





import java.util.List;
import java.util.ArrayList;

public class afpText_PMC extends structuredField {

    private String PMCid;



    public afpText_PMC(
        String PMCid    ) {
        super(
        );
        this.PMCid = PMCid;
    }


    public String getPmcid() {
        return PMCid;
    }

    public void setPmcid(String PMCid) {
        this.PMCid = PMCid;
    }


}