





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String Lat;
    private String Email;
    private String Long;
    private int ID;
    private int Gender;
    private String PhoneNumeber;
    private String Ssn;
    private String Password;
    private String InsuranceNumber;
    private String Last_Seen;
    private String Balance;
    private String Image;
    private String Name;



    public Person(
        String Lat,        String Email,        String Long,        int ID,        int Gender,        String PhoneNumeber,        String Ssn,        String Password,        String InsuranceNumber,        String Last_Seen,        String Balance,        String Image,        String Name    ) {
        this.Lat = Lat;
        this.Email = Email;
        this.Long = Long;
        this.ID = ID;
        this.Gender = Gender;
        this.PhoneNumeber = PhoneNumeber;
        this.Ssn = Ssn;
        this.Password = Password;
        this.InsuranceNumber = InsuranceNumber;
        this.Last_Seen = Last_Seen;
        this.Balance = Balance;
        this.Image = Image;
        this.Name = Name;
    }


    public String getLat() {
        return Lat;
    }

    public void setLat(String Lat) {
        this.Lat = Lat;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getLong() {
        return Long;
    }

    public void setLong(String Long) {
        this.Long = Long;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getGender() {
        return Gender;
    }

    public void setGender(int Gender) {
        this.Gender = Gender;
    }
    public String getPhonenumeber() {
        return PhoneNumeber;
    }

    public void setPhonenumeber(String PhoneNumeber) {
        this.PhoneNumeber = PhoneNumeber;
    }
    public String getSsn() {
        return Ssn;
    }

    public void setSsn(String Ssn) {
        this.Ssn = Ssn;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getInsurancenumber() {
        return InsuranceNumber;
    }

    public void setInsurancenumber(String InsuranceNumber) {
        this.InsuranceNumber = InsuranceNumber;
    }
    public String getLast_seen() {
        return Last_Seen;
    }

    public void setLast_seen(String Last_Seen) {
        this.Last_Seen = Last_Seen;
    }
    public String getBalance() {
        return Balance;
    }

    public void setBalance(String Balance) {
        this.Balance = Balance;
    }
    public String getImage() {
        return Image;
    }

    public void setImage(String Image) {
        this.Image = Image;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}