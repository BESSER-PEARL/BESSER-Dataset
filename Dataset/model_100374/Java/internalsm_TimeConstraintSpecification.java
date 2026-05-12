





import java.util.List;
import java.util.ArrayList;

public class internalsm_TimeConstraintSpecification  {

    private String expectedLength;
    private String id;
    private String stopTimestamp;
    private String startTimestamp;





    private internalsm_TimeConstraint internalsm_timeconstraint;


    public internalsm_TimeConstraintSpecification(
        String expectedLength,        String id,        String stopTimestamp,        String startTimestamp    ) {
        this.expectedLength = expectedLength;
        this.id = id;
        this.stopTimestamp = stopTimestamp;
        this.startTimestamp = startTimestamp;
    }


    public String getExpectedlength() {
        return expectedLength;
    }

    public void setExpectedlength(String expectedLength) {
        this.expectedLength = expectedLength;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStoptimestamp() {
        return stopTimestamp;
    }

    public void setStoptimestamp(String stopTimestamp) {
        this.stopTimestamp = stopTimestamp;
    }
    public String getStarttimestamp() {
        return startTimestamp;
    }

    public void setStarttimestamp(String startTimestamp) {
        this.startTimestamp = startTimestamp;
    }

    public internalsm_TimeConstraint getInternalsm_timeconstraint() {
        return internalsm_timeconstraint;
    }

    public void setInternalsm_timeconstraint(internalsm_TimeConstraint internalsm_timeconstraint) {
        this.internalsm_timeconstraint = internalsm_timeconstraint;
    }

}