





import java.util.List;
import java.util.ArrayList;

public class model_Bank  {

    private String address;
    private String customerMap;
    private String name;





    private List<model_Account> model_accounts;


    public model_Bank(
        String address,        String customerMap,        String name    ) {
        this.address = address;
        this.customerMap = customerMap;
        this.name = name;
        this.model_accounts = new ArrayList<>();
    }

    public model_Bank(
        String address,        String customerMap,        String name        ArrayList<model_Account> model_accounts    ) {
        this.address = address;
        this.customerMap = customerMap;
        this.name = name;
        this.model_accounts = model_accounts;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getCustomermap() {
        return customerMap;
    }

    public void setCustomermap(String customerMap) {
        this.customerMap = customerMap;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model_Account> getModel_accounts() {
        return model_accounts;
    }

    public void addModel_account(Model_account model_account) {
        this.model_accounts.add(model_account);
    }

}