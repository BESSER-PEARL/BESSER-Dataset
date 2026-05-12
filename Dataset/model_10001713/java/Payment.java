





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String amount;





    private Sale sale;




    private List<SUID> suids;


    public Payment(
        String amount    ) {
        this.amount = amount;
        this.suids = new ArrayList<>();
    }

    public Payment(
        String amount        ArrayList<SUID> suids    ) {
        this.amount = amount;
        this.suids = suids;
    }

    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }

    public Sale getSale() {
        return sale;
    }

    public void setSale(Sale sale) {
        this.sale = sale;
    }
    public List<SUID> getSuids() {
        return suids;
    }

    public void addSuid(Suid suid) {
        this.suids.add(suid);
    }

}