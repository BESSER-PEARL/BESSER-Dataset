





import java.util.List;
import java.util.ArrayList;

public class transaction_Payee  {

    private String country;
    private String city;
    private String email;
    private String phoneNum;
    private String accountNum;
    private String address2;
    private String name;
    private String zipcode;
    private String state;
    private String address1;





    private List<transaction_PaybillsTransaction> transaction_paybillstransactions;


    public transaction_Payee(
        String country,        String city,        String email,        String phoneNum,        String accountNum,        String address2,        String name,        String zipcode,        String state,        String address1    ) {
        this.country = country;
        this.city = city;
        this.email = email;
        this.phoneNum = phoneNum;
        this.accountNum = accountNum;
        this.address2 = address2;
        this.name = name;
        this.zipcode = zipcode;
        this.state = state;
        this.address1 = address1;
        this.transaction_paybillstransactions = new ArrayList<>();
    }

    public transaction_Payee(
        String country,        String city,        String email,        String phoneNum,        String accountNum,        String address2,        String name,        String zipcode,        String state,        String address1        ArrayList<transaction_PaybillsTransaction> transaction_paybillstransactions    ) {
        this.country = country;
        this.city = city;
        this.email = email;
        this.phoneNum = phoneNum;
        this.accountNum = accountNum;
        this.address2 = address2;
        this.name = name;
        this.zipcode = zipcode;
        this.state = state;
        this.address1 = address1;
        this.transaction_paybillstransactions = transaction_paybillstransactions;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPhonenum() {
        return phoneNum;
    }

    public void setPhonenum(String phoneNum) {
        this.phoneNum = phoneNum;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public String getAddress2() {
        return address2;
    }

    public void setAddress2(String address2) {
        this.address2 = address2;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }

    public List<transaction_PaybillsTransaction> getTransaction_paybillstransactions() {
        return transaction_paybillstransactions;
    }

    public void addTransaction_paybillstransaction(Transaction_paybillstransaction transaction_paybillstransaction) {
        this.transaction_paybillstransactions.add(transaction_paybillstransaction);
    }

}