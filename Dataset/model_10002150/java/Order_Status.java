





import java.util.List;
import java.util.ArrayList;

public class Order_Status  {

    private int Paid;
    private int Deliveried;
    private int Create;



    public Order_Status(
        int Paid,        int Deliveried,        int Create    ) {
        this.Paid = Paid;
        this.Deliveried = Deliveried;
        this.Create = Create;
    }


    public int getPaid() {
        return Paid;
    }

    public void setPaid(int Paid) {
        this.Paid = Paid;
    }
    public int getDeliveried() {
        return Deliveried;
    }

    public void setDeliveried(int Deliveried) {
        this.Deliveried = Deliveried;
    }
    public int getCreate() {
        return Create;
    }

    public void setCreate(int Create) {
        this.Create = Create;
    }


}