




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private LocalDate dateOfBirth;
    private String name;
    private String emailAddress;
    private String phoneNumber;
    private String address;





    private Login login;




    private List<account_Account> account_accounts;


    public Customer(
        LocalDate dateOfBirth,        String name,        String emailAddress,        String phoneNumber,        String address    ) {
        this.dateOfBirth = dateOfBirth;
        this.name = name;
        this.emailAddress = emailAddress;
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.account_accounts = new ArrayList<>();
    }

    public Customer(
        LocalDate dateOfBirth,        String name,        String emailAddress,        String phoneNumber,        String address        ArrayList<account_Account> account_accounts    ) {
        this.dateOfBirth = dateOfBirth;
        this.name = name;
        this.emailAddress = emailAddress;
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.account_accounts = account_accounts;
    }

    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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