





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String taxId;
    private String name;





    private Bank bank;


    public Customer(
        String taxId,        String name    ) {
        this.taxId = taxId;
        this.name = name;
    }


    public String getTaxid() {
        return taxId;
    }

    public void setTaxid(String taxId) {
        this.taxId = taxId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}