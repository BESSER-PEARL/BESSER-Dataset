




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String phoneNumber;
    private String name;
    private String address;
    private String emailAddress;
    private LocalDate dateOfBirth;





    private Login login;




    private List<account_Account> account_accounts;


    public Customer(
        String phoneNumber,        String name,        String address,        String emailAddress,        LocalDate dateOfBirth    ) {
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.address = address;
        this.emailAddress = emailAddress;
        this.dateOfBirth = dateOfBirth;
        this.account_accounts = new ArrayList<>();
    }

    public Customer(
        String phoneNumber,        String name,        String address,        String emailAddress,        LocalDate dateOfBirth        ArrayList<account_Account> account_accounts    ) {
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.address = address;
        this.emailAddress = emailAddress;
        this.dateOfBirth = dateOfBirth;
        this.account_accounts = account_accounts;
    }

    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }
    public List<account_Account> getAccount_accounts() {
        return account_accounts;
    }

    public void addAccount_account(Account_account account_account) {
        this.account_accounts.add(account_account);
    }

}