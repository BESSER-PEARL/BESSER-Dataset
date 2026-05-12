





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String username;
    private String balance;
    private String birthDate;
    private String referrer;
    private String phoneNumber;
    private String id;
    private None accountStatus;
    private int numberOfReferrals;
    private String referralCode;
    private int gender;
    private String avatar;
    private String email;



    public User(
        String username,        String balance,        String birthDate,        String referrer,        String phoneNumber,        String id,        None accountStatus,        int numberOfReferrals,        String referralCode,        int gender,        String avatar,        String email    ) {
        this.username = username;
        this.balance = balance;
        this.birthDate = birthDate;
        this.referrer = referrer;
        this.phoneNumber = phoneNumber;
        this.id = id;
        this.accountStatus = accountStatus;
        this.numberOfReferrals = numberOfReferrals;
        this.referralCode = referralCode;
        this.gender = gender;
        this.avatar = avatar;
        this.email = email;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }
    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }
    public String getReferrer() {
        return referrer;
    }

    public void setReferrer(String referrer) {
        this.referrer = referrer;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getAccountstatus() {
        return accountStatus;
    }

    public void setAccountstatus(None accountStatus) {
        this.accountStatus = accountStatus;
    }
    public int getNumberofreferrals() {
        return numberOfReferrals;
    }

    public void setNumberofreferrals(int numberOfReferrals) {
        this.numberOfReferrals = numberOfReferrals;
    }
    public String getReferralcode() {
        return referralCode;
    }

    public void setReferralcode(String referralCode) {
        this.referralCode = referralCode;
    }
    public int getGender() {
        return gender;
    }

    public void setGender(int gender) {
        this.gender = gender;
    }
    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}