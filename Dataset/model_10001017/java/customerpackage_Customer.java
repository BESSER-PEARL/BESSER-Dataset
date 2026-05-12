




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class customerpackage_Customer  {

    private LocalDate dateOfBirth;
    private String name;
    private String address;
    private String emailAddress;
    private String phoneNumber;





    private List<account_Account> account_accounts;


    public customerpackage_Customer(
        LocalDate dateOfBirth,        String name,        String address,        String emailAddress,        String phoneNumber    ) {
        this.dateOfBirth = dateOfBirth;
        this.name = name;
        this.address = address;
        this.emailAddress = emailAddress;
        this.phoneNumber = phoneNumber;
        this.account_accounts = new ArrayList<>();
    }

    public customerpackage_Customer(
        LocalDate dateOfBirth,        String name,        String address,        String emailAddress,        String phoneNumber        ArrayList<account_Account> account_accounts    ) {
        this.dateOfBirth = dateOfBirth;
        this.name = name;
        this.address = address;
        this.emailAddress = emailAddress;
        this.phoneNumber = phoneNumber;
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
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public List<account_Account> getAccount_accounts() {
        return account_accounts;
    }

    public void addAccount_account(Account_account account_account) {
        this.account_accounts.add(account_account);
    }

}