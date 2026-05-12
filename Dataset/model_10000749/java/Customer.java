




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String phoneNumber;
    private String emailAddress;
    private String name;
    private String address;
    private LocalDate dateOfBirth;





    private List<account_Account> account_accounts;


    public Customer(
        String phoneNumber,        String emailAddress,        String name,        String address,        LocalDate dateOfBirth    ) {
        this.phoneNumber = phoneNumber;
        this.emailAddress = emailAddress;
        this.name = name;
        this.address = address;
        this.dateOfBirth = dateOfBirth;
        this.account_accounts = new ArrayList<>();
    }

    public Customer(
        String phoneNumber,        String emailAddress,        String name,        String address,        LocalDate dateOfBirth        ArrayList<account_Account> account_accounts    ) {
        this.phoneNumber = phoneNumber;
        this.emailAddress = emailAddress;
        this.name = name;
        this.address = address;
        this.dateOfBirth = dateOfBirth;
        this.account_accounts = account_accounts;
    }

    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public List<account_Account> getAccount_accounts() {
        return account_accounts;
    }

    public void addAccount_account(Account_account account_account) {
        this.account_accounts.add(account_account);
    }

}