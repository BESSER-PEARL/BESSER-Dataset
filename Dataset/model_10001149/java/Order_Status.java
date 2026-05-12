





import java.util.List;
import java.util.ArrayList;

public class Order_Status  {

    private int Create;
    private int Deliveried;
    private int Paid;



    public Order_Status(
        int Create,        int Deliveried,        int Paid    ) {
        this.Create = Create;
        this.Deliveried = Deliveried;
        this.Paid = Paid;
    }


    public int getCreate() {
        return Create;
    }

    public void setCreate(int Create) {
        this.Create = Create;
    }
    public int getDeliveried() {
        return Deliveried;
    }

    public void setDeliveried(int Deliveried) {
        this.Deliveried = Deliveried;
    }
    public int getPaid() {
        return Paid;
    }

    public void setPaid(int Paid) {
        this.Paid = Paid;
    }


}