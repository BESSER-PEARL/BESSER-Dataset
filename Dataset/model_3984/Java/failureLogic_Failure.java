





import java.util.List;
import java.util.ArrayList;

public class failureLogic_Failure extends BaseElement {

    private String originType;
    private float failureRate;
    private String failureClass;
    private boolean isCcf;





    private List<failureLogic_Failure> failurelogic_failures;


    public failureLogic_Failure(
        String originType,        float failureRate,        String failureClass,        boolean isCcf    ) {
        super(
        );
        this.originType = originType;
        this.failureRate = failureRate;
        this.failureClass = failureClass;
        this.isCcf = isCcf;
        this.failurelogic_failures = new ArrayList<>();
    }

    public failureLogic_Failure(
        String originType,        float failureRate,        String failureClass,        boolean isCcf        ArrayList<failureLogic_Failure> failurelogic_failures    ) {
        this.originType = originType;
        this.failureRate = failureRate;
        this.failureClass = failureClass;
        this.isCcf = isCcf;
        this.failurelogic_failures = failurelogic_failures;
    }

    public String getOrigintype() {
        return originType;
    }

    public void setOrigintype(String originType) {
        this.originType = originType;
    }
    public float getFailurerate() {
        return failureRate;
    }

    public void setFailurerate(float failureRate) {
        this.failureRate = failureRate;
    }
    public String getFailureclass() {
        return failureClass;
    }

    public void setFailureclass(String failureClass) {
        this.failureClass = failureClass;
    }
    public boolean getIsccf() {
        return isCcf;
    }

    public void setIsccf(boolean isCcf) {
        this.isCcf = isCcf;
    }

    public List<failureLogic_Failure> getFailurelogic_failures() {
        return failurelogic_failures;
    }

    public void addFailurelogic_failure(Failurelogic_failure failurelogic_failure) {
        this.failurelogic_failures.add(failurelogic_failure);
    }

}