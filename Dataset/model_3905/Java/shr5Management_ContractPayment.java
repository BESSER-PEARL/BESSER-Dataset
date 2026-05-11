





import java.util.List;
import java.util.ArrayList;

public class shr5Management_ContractPayment extends DiaryEntry {

    private boolean payed;



    public shr5Management_ContractPayment(
        boolean payed    ) {
        super(
        );
        this.payed = payed;
    }


    public boolean getPayed() {
        return payed;
    }

    public void setPayed(boolean payed) {
        this.payed = payed;
    }


}