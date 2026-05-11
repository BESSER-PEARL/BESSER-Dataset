





import java.util.List;
import java.util.ArrayList;

public class remember_InvoiceSpecification  {

    private int month;





    private remember_TimeSpent remember_timespent;




    private List<remember_TimeSpent> remember_timespents;


    public remember_InvoiceSpecification(
        int month    ) {
        this.month = month;
        this.remember_timespents = new ArrayList<>();
    }

    public remember_InvoiceSpecification(
        int month        ArrayList<remember_TimeSpent> remember_timespents    ) {
        this.month = month;
        this.remember_timespents = remember_timespents;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }

    public remember_TimeSpent getRemember_timespent() {
        return remember_timespent;
    }

    public void setRemember_timespent(remember_TimeSpent remember_timespent) {
        this.remember_timespent = remember_timespent;
    }
    public List<remember_TimeSpent> getRemember_timespents() {
        return remember_timespents;
    }

    public void addRemember_timespent(Remember_timespent remember_timespent) {
        this.remember_timespents.add(remember_timespent);
    }

}