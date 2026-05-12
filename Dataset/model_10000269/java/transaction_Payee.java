





import java.util.List;
import java.util.ArrayList;

public class transaction_Payee  {

    private String state;
    private String zipcode;
    private String email;
    private String country;
    private String address2;
    private String city;
    private String accountNum;
    private String userID;
    private String name;
    private String address1;
    private String phoneNum;





    private List<transaction_PaybillsTransaction> transaction_paybillstransactions;


    public transaction_Payee(
        String state,        String zipcode,        String email,        String country,        String address2,        String city,        String accountNum,        String userID,        String name,        String address1,        String phoneNum    ) {
        this.state = state;
        this.zipcode = zipcode;
        this.email = email;
        this.country = country;
        this.address2 = address2;
        this.city = city;
        this.accountNum = accountNum;
        this.userID = userID;
        this.name = name;
        this.address1 = address1;
        this.phoneNum = phoneNum;
        this.transaction_paybillstransactions = new ArrayList<>();
    }

    public transaction_Payee(
        String state,        String zipcode,        String email,        String country,        String address2,        String city,        String accountNum,        String userID,        String name,        String address1,        String phoneNum        ArrayList<transaction_PaybillsTransaction> transaction_paybillstransactions    ) {
        this.state = state;
        this.zipcode = zipcode;
        this.email = email;
        this.country = country;
        this.address2 = address2;
        this.city = city;
        this.accountNum = accountNum;
        this.userID = userID;
        this.name = name;
        this.address1 = address1;
        this.phoneNum = phoneNum;
        this.transaction_paybillstransactions = transaction_paybillstransactions;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getAddress2() {
        return address2;
    }

    public void setAddress2(String address2) {
        this.address2 = address2;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }
    public String getPhonenum() {
        return phoneNum;
    }

    public void setPhonenum(String phoneNum) {
        this.phoneNum = phoneNum;
    }

    public List<transaction_PaybillsTransaction> getTransaction_paybillstransactions() {
        return transaction_paybillstransactions;
    }

    public void addTransaction_paybillstransaction(Transaction_paybillstransaction transaction_paybillstransaction) {
        this.transaction_paybillstransactions.add(transaction_paybillstransaction);
    }

}