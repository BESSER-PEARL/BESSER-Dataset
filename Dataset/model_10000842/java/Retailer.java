




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Retailer  {

    private LocalDate dateOfBirth;
    private int userId;
    private String Photo;
    private String emailId;
    private String address;
    private String name;
    private int CardInfo;
    private int phone;





    private CardInfo cardinfo;


    public Retailer(
        LocalDate dateOfBirth,        int userId,        String Photo,        String emailId,        String address,        String name,        int CardInfo,        int phone    ) {
        this.dateOfBirth = dateOfBirth;
        this.userId = userId;
        this.Photo = Photo;
        this.emailId = emailId;
        this.address = address;
        this.name = name;
        this.CardInfo = CardInfo;
        this.phone = phone;
    }


    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public int getUserid() {
        return userId;
    }

    public void setUserid(int userId) {
        this.userId = userId;
    }
    public String getPhoto() {
        return Photo;
    }

    public void setPhoto(String Photo) {
        this.Photo = Photo;
    }
    public String getEmailid() {
        return emailId;
    }

    public void setEmailid(String emailId) {
        this.emailId = emailId;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCardinfo() {
        return CardInfo;
    }

    public void setCardinfo(int CardInfo) {
        this.CardInfo = CardInfo;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }

    public CardInfo getCardinfo() {
        return cardinfo;
    }

    public void setCardinfo(CardInfo cardinfo) {
        this.cardinfo = cardinfo;
    }

}