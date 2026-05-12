




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Customer  {

    private LocalDate dateOfBirth;
    private String phoneNumber;
    private String address;
    private String emailAddress;
    private String name;





    private mypackage_Login mypackage_login;




    private List<account_Account> account_accounts;


    public mypackage_Customer(
        LocalDate dateOfBirth,        String phoneNumber,        String address,        String emailAddress,        String name    ) {
        this.dateOfBirth = dateOfBirth;
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.emailAddress = emailAddress;
        this.name = name;
        this.account_accounts = new ArrayList<>();
    }

    public mypackage_Customer(
        LocalDate dateOfBirth,        String phoneNumber,        String address,        String emailAddress,        String name        ArrayList<account_Account> account_accounts    ) {
        this.dateOfBirth = dateOfBirth;
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.emailAddress = emailAddress;
        this.name = name;
        this.account_accounts = account_accounts;
    }

    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
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
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mypackage_Login getMypackage_login() {
        return mypackage_login;
    }

    public void setMypackage_login(mypackage_Login mypackage_login) {
        this.mypackage_login = mypackage_login;
    }
    public List<account_Account> getAccount_accounts() {
        return account_accounts;
    }

    public void addAccount_account(Account_account account_account) {
        this.account_accounts.add(account_account);
    }

}