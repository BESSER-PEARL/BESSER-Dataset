





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaStep extends GaStep {

    private String schSlack;
    private String preemptT;
    private String readyT;
    private String numberSelfSuspensions;
    private String selfSuspensionBlocking;
    private String nonpreemptionBlocking;
    private String deadline;
    private String spareCap;



    public MARTE_SAM_SaStep(
        String schSlack,        String preemptT,        String readyT,        String numberSelfSuspensions,        String selfSuspensionBlocking,        String nonpreemptionBlocking,        String deadline,        String spareCap    ) {
        super(
        );
        this.schSlack = schSlack;
        this.preemptT = preemptT;
        this.readyT = readyT;
        this.numberSelfSuspensions = numberSelfSuspensions;
        this.selfSuspensionBlocking = selfSuspensionBlocking;
        this.nonpreemptionBlocking = nonpreemptionBlocking;
        this.deadline = deadline;
        this.spareCap = spareCap;
    }


    public String getSchslack() {
        return schSlack;
    }

    public void setSchslack(String schSlack) {
        this.schSlack = schSlack;
    }
    public String getPreemptt() {
        return preemptT;
    }

    public void setPreemptt(String preemptT) {
        this.preemptT = preemptT;
    }
    public String getReadyt() {
        return readyT;
    }

    public void setReadyt(String readyT) {
        this.readyT = readyT;
    }
    public String getNumberselfsuspensions() {
        return numberSelfSuspensions;
    }

    public void setNumberselfsuspensions(String numberSelfSuspensions) {
        this.numberSelfSuspensions = numberSelfSuspensions;
    }
    public String getSelfsuspensionblocking() {
        return selfSuspensionBlocking;
    }

    public void setSelfsuspensionblocking(String selfSuspensionBlocking) {
        this.selfSuspensionBlocking = selfSuspensionBlocking;
    }
    public String getNonpreemptionblocking() {
        return nonpreemptionBlocking;
    }

    public void setNonpreemptionblocking(String nonpreemptionBlocking) {
        this.nonpreemptionBlocking = nonpreemptionBlocking;
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