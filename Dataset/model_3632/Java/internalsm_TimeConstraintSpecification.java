





import java.util.List;
import java.util.ArrayList;

public class internalsm_TimeConstraintSpecification  {

    private String id;
    private String startTimestamp;
    private String expectedLength;
    private String stopTimestamp;





    private internalsm_TimeConstraint internalsm_timeconstraint;


    public internalsm_TimeConstraintSpecification(
        String id,        String startTimestamp,        String expectedLength,        String stopTimestamp    ) {
        this.id = id;
        this.startTimestamp = startTimestamp;
        this.expectedLength = expectedLength;
        this.stopTimestamp = stopTimestamp;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStarttimestamp() {
        return startTimestamp;
    }

    public void setStarttimestamp(String startTimestamp) {
        this.startTimestamp = startTimestamp;
    }
    public String getExpectedlength() {
        return expectedLength;
    }

    public void setExpectedlength(String expectedLength) {
        this.expectedLength = expectedLength;
    }
    public String getStoptimestamp() {
        return stopTimestamp;
    }

    public void setStoptimestamp(String stopTimestamp) {
        this.stopTimestamp = stopTimestamp;
    }

    public internalsm_TimeConstraint getInternalsm_timeconstraint() {
        return internalsm_timeconstraint;
    }

    public void setInternalsm_timeconstraint(internalsm_TimeConstraint internalsm_timeconstraint) {
        this.internalsm_timeconstraint = internalsm_timeconstraint;
    }

}