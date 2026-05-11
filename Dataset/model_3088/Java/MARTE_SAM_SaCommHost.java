





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaCommHost extends GaCommHost {

    private String isSched;
    private String schSlack;



    public MARTE_SAM_SaCommHost(
        String isSched,        String schSlack    ) {
        super(
        );
        this.isSched = isSched;
        this.schSlack = schSlack;
    }


    public String getIssched() {
        return isSched;
    }

    public void setIssched(String isSched) {
        this.isSched = isSched;
    }
    public String getSchslack() {
        return schSlack;
    }

    public void setSchslack(String schSlack) {
        this.schSlack = schSlack;
    }


}