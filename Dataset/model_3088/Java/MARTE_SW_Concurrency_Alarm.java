





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Concurrency_Alarm extends InterruptResource {

    private String isWatchdog;





    private List<SW_Concurrency_MARTE_TypedElement> sw_concurrency_marte_typedelements;


    public MARTE_SW_Concurrency_Alarm(
        String isWatchdog    ) {
        super(
        );
        this.isWatchdog = isWatchdog;
        this.sw_concurrency_marte_typedelements = new ArrayList<>();
    }

    public MARTE_SW_Concurrency_Alarm(
        String isWatchdog        ArrayList<SW_Concurrency_MARTE_TypedElement> sw_concurrency_marte_typedelements    ) {
        this.isWatchdog = isWatchdog;
        this.sw_concurrency_marte_typedelements = sw_concurrency_marte_typedelements;
    }

    public String getIswatchdog() {
        return isWatchdog;
    }

    public void setIswatchdog(String isWatchdog) {
        this.isWatchdog = isWatchdog;
    }

    public List<SW_Concurrency_MARTE_TypedElement> getSw_concurrency_marte_typedelements() {
        return sw_concurrency_marte_typedelements;
    }

    public void addSw_concurrency_marte_typedelement(Sw_concurrency_marte_typedelement sw_concurrency_marte_typedelement) {
        this.sw_concurrency_marte_typedelements.add(sw_concurrency_marte_typedelement);
    }

}