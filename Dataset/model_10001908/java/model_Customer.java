





import java.util.List;
import java.util.ArrayList;

public class model_Customer  {

    private String name;
    private String accounts;
    private String password;
    private int id;
    private String address;
    private String username;
    private String dob;





    private List<model_AccountAction> model_accountactions;




    private model_Bank model_bank;




    private List<model_Account> model_accounts;


    public model_Customer(
        String name,        String accounts,        String password,        int id,        String address,        String username,        String dob    ) {
        this.name = name;
        this.accounts = accounts;
        this.password = password;
        this.id = id;
        this.address = address;
        this.username = username;
        this.dob = dob;
        this.model_accountactions = new ArrayList<>();
        this.model_accounts = new ArrayList<>();
    }

    public model_Customer(
        String name,        String accounts,        String password,        int id,        String address,        String username,        String dob        ArrayList<model_AccountAction> model_accountactions,        ArrayList<model_Account> model_accounts    ) {
        this.name = name;
        this.accounts = accounts;
        this.password = password;
        this.id = id;
        this.address = address;
        this.username = username;
        this.dob = dob;
        this.model_accountactions = model_accountactions;
        this.model_accounts = model_accounts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccounts() {
        return accounts;
    }

    public void setAccounts(String accounts) {
        this.accounts = accounts;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getDob() {
        return dob;
    }

    public void setDob(String dob) {
        this.dob = dob;
    }

    public List<model_AccountAction> getModel_accountactions() {
        return model_accountactions;
    }

    public void addModel_accountaction(Model_accountaction model_accountaction) {
        this.model_accountactions.add(model_accountaction);
    }
    public model_Bank getModel_bank() {
        return model_bank;
    }

    public void setModel_bank(model_Bank model_bank) {
        this.model_bank = model_bank;
    }
    public List<model_Account> getModel_accounts() {
        return model_accounts;
    }

    public void addModel_account(Model_account model_account) {
        this.model_accounts.add(model_account);
    }

}