





import java.util.List;
import java.util.ArrayList;

public class accounting_Account  {

    private String name;





    private accounting_AccountGroup accounting_accountgroup;


    public accounting_Account(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public accounting_AccountGroup getAccounting_accountgroup() {
        return accounting_accountgroup;
    }

    public void setAccounting_accountgroup(accounting_AccountGroup accounting_accountgroup) {
        this.accounting_accountgroup = accounting_accountgroup;
    }

}