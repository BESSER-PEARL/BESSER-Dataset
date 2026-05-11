





import java.util.List;
import java.util.ArrayList;

public class MARTE_Time_ClockConstraint extends Time_TimedElement, NFPs_NfpConstraint {

    private String isChronometricBased;
    private boolean isPrecedenceBased;
    private String isCoincidenceBased;



    public MARTE_Time_ClockConstraint(
        String isChronometricBased,        boolean isPrecedenceBased,        String isCoincidenceBased    ) {
        super(
        );
        this.isChronometricBased = isChronometricBased;
        this.isPrecedenceBased = isPrecedenceBased;
        this.isCoincidenceBased = isCoincidenceBased;
    }


    public String getIschronometricbased() {
        return isChronometricBased;
    }

    public void setIschronometricbased(String isChronometricBased) {
        this.isChronometricBased = isChronometricBased;
    }
    public boolean getIsprecedencebased() {
        return isPrecedenceBased;
    }

    public void setIsprecedencebased(boolean isPrecedenceBased) {
        this.isPrecedenceBased = isPrecedenceBased;
    }
    public String getIscoincidencebased() {
        return isCoincidenceBased;
    }

    public void setIscoincidencebased(String isCoincidenceBased) {
        this.isCoincidenceBased = isCoincidenceBased;
    }


}