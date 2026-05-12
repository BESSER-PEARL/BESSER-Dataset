





import java.util.List;
import java.util.ArrayList;

public class Order_Status  {

    private int Deliveried;
    private int Paid;
    private int Create;



    public Order_Status(
        int Deliveried,        int Paid,        int Create    ) {
        this.Deliveried = Deliveried;
        this.Paid = Paid;
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
    public int getCreate() {
        return Create;
    }

    public void setCreate(int Create) {
        this.Create = Create;
    }


}