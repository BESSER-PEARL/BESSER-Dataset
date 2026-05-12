




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String emailAddress;
    private String name;
    private String phoneNumber;
    private LocalDate dateOfBirth;
    private String address;





    private List<account_Account> account_accounts;


    public Customer(
        String emailAddress,        String name,        String phoneNumber,        LocalDate dateOfBirth,        String address    ) {
        this.emailAddress = emailAddress;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
        this.account_accounts = new ArrayList<>();
    }

    public Customer(
        String emailAddress,        String name,        String phoneNumber,        LocalDate dateOfBirth,        String address        ArrayList<account_Account> account_accounts    ) {
        this.emailAddress = emailAddress;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
        this.account_accounts = account_accounts;
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
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<account_Account> getAccount_accounts() {
        return account_accounts;
    }

    public void addAccount_account(Account_account account_account) {
        this.account_accounts.add(account_account);
    }

}