





import java.util.List;
import java.util.ArrayList;

public class nocollectionowner_Customer  {

    private String telephoneNr;
    private String hotel;
    private String address;
    private String familyName;
    private String surname;
    private String comments;



    public nocollectionowner_Customer(
        String telephoneNr,        String hotel,        String address,        String familyName,        String surname,        String comments    ) {
        this.telephoneNr = telephoneNr;
        this.hotel = hotel;
        this.address = address;
        this.familyName = familyName;
        this.surname = surname;
        this.comments = comments;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getFamilyname() {
        return familyName;
    }

    public void setFamilyname(String familyName) {
        this.familyName = familyName;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }


}