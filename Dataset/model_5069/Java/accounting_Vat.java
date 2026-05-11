





import java.util.List;
import java.util.ArrayList;

public class accounting_Vat  {

    private String name;
    private String rate;





    private accounting_Accounting accounting_accounting;


    public accounting_Vat(
        String name,        String rate    ) {
        this.name = name;
        this.rate = rate;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRate() {
        return rate;
    }

    public void setRate(String rate) {
        this.rate = rate;
    }

    public accounting_Accounting getAccounting_accounting() {
        return accounting_accounting;
    }

    public void setAccounting_accounting(accounting_Accounting accounting_accounting) {
        this.accounting_accounting = accounting_accounting;
    }

}