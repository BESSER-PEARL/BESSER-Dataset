





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaCommStep extends GaCommStep {

    private String schSlack;
    private String deadline;
    private String spareCap;



    public MARTE_SAM_SaCommStep(
        String schSlack,        String deadline,        String spareCap    ) {
        super(
        );
        this.schSlack = schSlack;
        this.deadline = deadline;
        this.spareCap = spareCap;
    }


    public String getSchslack() {
        return schSlack;
    }

    public void setSchslack(String schSlack) {
        this.schSlack = schSlack;
    }
    public String getDeadline() {
        return deadline;
    }

    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }
    public String getSparecap() {
        return spareCap;
    }

    public void setSparecap(String spareCap) {
        this.spareCap = spareCap;
    }


}