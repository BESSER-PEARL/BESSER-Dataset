





import java.util.List;
import java.util.ArrayList;

public class eShop_Sale  {

    private int id;
    private boolean paid;
    private int amount;



    public eShop_Sale(
        int id,        boolean paid,        int amount    ) {
        this.id = id;
        this.paid = paid;
        this.amount = amount;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getPaid() {
        return paid;
    }

    public void setPaid(boolean paid) {
        this.paid = paid;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }


}