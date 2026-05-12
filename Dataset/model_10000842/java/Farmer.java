




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Farmer  {

    private String type;
    private String emailId;
    private LocalDate dateOfBirth;
    private String CardInfo;
    private String address;
    private int accountInfoID;
    private int phone;
    private String name;
    private int userId;



    public Farmer(
        String type,        String emailId,        LocalDate dateOfBirth,        String CardInfo,        String address,        int accountInfoID,        int phone,        String name,        int userId    ) {
        this.type = type;
        this.emailId = emailId;
        this.dateOfBirth = dateOfBirth;
        this.CardInfo = CardInfo;
        this.address = address;
        this.accountInfoID = accountInfoID;
        this.phone = phone;
        this.name = name;
        this.userId = userId;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getEmailid() {
        return emailId;
    }

    public void setEmailid(String emailId) {
        this.emailId = emailId;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getCardinfo() {
        return CardInfo;
    }

    public void setCardinfo(String CardInfo) {
        this.CardInfo = CardInfo;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getAccountinfoid() {
        return accountInfoID;
    }

    public void setAccountinfoid(int accountInfoID) {
        this.accountInfoID = accountInfoID;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getUserid() {
        return userId;
    }

    public void setUserid(int userId) {
        this.userId = userId;
    }


}