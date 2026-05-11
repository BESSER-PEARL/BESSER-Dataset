





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FMEA extends FailureModel {

    private String type;





    private List<failureLogic_FMEAEntry> failurelogic_fmeaentrys;


    public failureLogic_FMEA(
        String type    ) {
        super(
        );
        this.type = type;
        this.failurelogic_fmeaentrys = new ArrayList<>();
    }

    public failureLogic_FMEA(
        String type        ArrayList<failureLogic_FMEAEntry> failurelogic_fmeaentrys    ) {
        this.type = type;
        this.failurelogic_fmeaentrys = failurelogic_fmeaentrys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<failureLogic_FMEAEntry> getFailurelogic_fmeaentrys() {
        return failurelogic_fmeaentrys;
    }

    public void addFailurelogic_fmeaentry(Failurelogic_fmeaentry failurelogic_fmeaentry) {
        this.failurelogic_fmeaentrys.add(failurelogic_fmeaentry);
    }

}