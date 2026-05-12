





import java.util.List;
import java.util.ArrayList;

public class data_CustomerProfileRepository  {

    private int numAccounts;
    private String customerProfiles;



    public data_CustomerProfileRepository(
        int numAccounts,        String customerProfiles    ) {
        this.numAccounts = numAccounts;
        this.customerProfiles = customerProfiles;
    }


    public int getNumaccounts() {
        return numAccounts;
    }

    public void setNumaccounts(int numAccounts) {
        this.numAccounts = numAccounts;
    }
    public String getCustomerprofiles() {
        return customerProfiles;
    }

    public void setCustomerprofiles(String customerProfiles) {
        this.customerProfiles = customerProfiles;
    }


}