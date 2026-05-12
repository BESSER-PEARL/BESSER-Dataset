





import java.util.List;
import java.util.ArrayList;

public class bank  {

    private String bank_name;





    private income_manager income_manager;


    public bank(
        String bank_name    ) {
        this.bank_name = bank_name;
    }


    public String getBank_name() {
        return bank_name;
    }

    public void setBank_name(String bank_name) {
        this.bank_name = bank_name;
    }

    public income_manager getIncome_manager() {
        return income_manager;
    }

    public void setIncome_manager(income_manager income_manager) {
        this.income_manager = income_manager;
    }

}