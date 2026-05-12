





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String Type;
    private String BranchLocation;
    private String Owned_by;





    private Debit_Card debit_card;


    public Account(
        String Type,        String BranchLocation,        String Owned_by    ) {
        this.Type = Type;
        this.BranchLocation = BranchLocation;
        this.Owned_by = Owned_by;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getBranchlocation() {
        return BranchLocation;
    }

    public void setBranchlocation(String BranchLocation) {
        this.BranchLocation = BranchLocation;
    }
    public String getOwned_by() {
        return Owned_by;
    }

    public void setOwned_by(String Owned_by) {
        this.Owned_by = Owned_by;
    }

    public Debit_Card getDebit_card() {
        return debit_card;
    }

    public void setDebit_card(Debit_Card debit_card) {
        this.debit_card = debit_card;
    }

}