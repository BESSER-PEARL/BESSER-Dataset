





import java.util.List;
import java.util.ArrayList;

public class Worker  {

    private String Cashier;
    private String Waitor;
    private String Cook;



    public Worker(
        String Cashier,        String Waitor,        String Cook    ) {
        this.Cashier = Cashier;
        this.Waitor = Waitor;
        this.Cook = Cook;
    }


    public String getCashier() {
        return Cashier;
    }

    public void setCashier(String Cashier) {
        this.Cashier = Cashier;
    }
    public String getWaitor() {
        return Waitor;
    }

    public void setWaitor(String Waitor) {
        this.Waitor = Waitor;
    }
    public String getCook() {
        return Cook;
    }

    public void setCook(String Cook) {
        this.Cook = Cook;
    }


}