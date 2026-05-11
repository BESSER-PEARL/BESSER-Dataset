





import java.util.List;
import java.util.ArrayList;

public class shop_Customer  {

    private String telephoneNr;
    private String hotel;
    private String familyName;
    private String comments;
    private String address;
    private String surname;



    public shop_Customer(
        String telephoneNr,        String hotel,        String familyName,        String comments,        String address,        String surname    ) {
        this.telephoneNr = telephoneNr;
        this.hotel = hotel;
        this.familyName = familyName;
        this.comments = comments;
        this.address = address;
        this.surname = surname;
    }


    public String getTelephonenr() {
        return telephoneNr;
    }

    public void setTelephonenr(String telephoneNr) {
        this.telephoneNr = telephoneNr;
    }
    public String getHotel() {
        return hotel;
    }

    public void setHotel(String hotel) {
        this.hotel = hotel;
    }
    public String getFamilyname() {
        return familyName;
    }

    public void setFamilyname(String familyName) {
        this.familyName = familyName;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }


}