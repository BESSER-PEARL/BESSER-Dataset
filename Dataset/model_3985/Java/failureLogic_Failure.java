





import java.util.List;
import java.util.ArrayList;

public class failureLogic_Failure extends BaseElement {

    private String originType;
    private boolean isCcf;
    private String failureClass;
    private float failureRate;





    private List<failureLogic_Failure> failurelogic_failures;




    private failureLogic_FailureModel failurelogic_failuremodel;


    public failureLogic_Failure(
        String originType,        boolean isCcf,        String failureClass,        float failureRate    ) {
        super(
        );
        this.originType = originType;
        this.isCcf = isCcf;
        this.failureClass = failureClass;
        this.failureRate = failureRate;
        this.failurelogic_failures = new ArrayList<>();
    }

    public failureLogic_Failure(
        String originType,        boolean isCcf,        String failureClass,        float failureRate        ArrayList<failureLogic_Failure> failurelogic_failures    ) {
        this.originType = originType;
        this.isCcf = isCcf;
        this.failureClass = failureClass;
        this.failureRate = failureRate;
        this.failurelogic_failures = failurelogic_failures;
    }

    public String getOrigintype() {
        return originType;
    }

    public void setOrigintype(String originType) {
        this.originType = originType;
    }
    public boolean getIsccf() {
        return isCcf;
    }

    public void setIsccf(boolean isCcf) {
        this.isCcf = isCcf;
    }
    public String getFailureclass() {
        return failureClass;
    }

    public void setFailureclass(String failureClass) {
        this.failureClass = failureClass;
    }
    public float getFailurerate() {
        return failureRate;
    }

    public void setFailurerate(float failureRate) {
        this.failureRate = failureRate;
    }

    public List<failureLogic_Failure> getFailurelogic_failures() {
        return failurelogic_failures;
    }

    public void addFailurelogic_failure(Failurelogic_failure failurelogic_failure) {
        this.failurelogic_failures.add(failurelogic_failure);
    }
    public failureLogic_FailureModel getFailurelogic_failuremodel() {
        return failurelogic_failuremodel;
    }

    public void setFailurelogic_failuremodel(failureLogic_FailureModel failurelogic_failuremodel) {
        this.failurelogic_failuremodel = failurelogic_failuremodel;
    }

}