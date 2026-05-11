





import java.util.List;
import java.util.ArrayList;

public class MARTE_Time_ClockConstraint extends Time_TimedElement, NFPs_NfpConstraint {

    private String isCoincidenceBased;
    private boolean isPrecedenceBased;
    private String isChronometricBased;



    public MARTE_Time_ClockConstraint(
        String isCoincidenceBased,        boolean isPrecedenceBased,        String isChronometricBased    ) {
        super(
        );
        this.isCoincidenceBased = isCoincidenceBased;
        this.isPrecedenceBased = isPrecedenceBased;
        this.isChronometricBased = isChronometricBased;
    }


    public String getIscoincidencebased() {
        return isCoincidenceBased;
    }

    public void setIscoincidencebased(String isCoincidenceBased) {
        this.isCoincidenceBased = isCoincidenceBased;
    }
    public boolean getIsprecedencebased() {
        return isPrecedenceBased;
    }

    public void setIsprecedencebased(boolean isPrecedenceBased) {
        this.isPrecedenceBased = isPrecedenceBased;
    }
    public String getIschronometricbased() {
        return isChronometricBased;
    }

    public void setIschronometricbased(String isChronometricBased) {
        this.isChronometricBased = isChronometricBased;
    }


}