





import java.util.List;
import java.util.ArrayList;

public class Branch  {

    private String City;
    private String Branch_code;





    private Bank bank;


    public Branch(
        String City,        String Branch_code    ) {
        this.City = City;
        this.Branch_code = Branch_code;
    }


    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getBranch_code() {
        return Branch_code;
    }

    public void setBranch_code(String Branch_code) {
        this.Branch_code = Branch_code;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}