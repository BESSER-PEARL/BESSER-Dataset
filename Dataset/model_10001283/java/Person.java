





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private int ID;
    private String InsuranceNumber;
    private String Email;
    private String Balance;
    private String Image;
    private String Ssn;
    private String Last_Seen;
    private String Name;
    private int Gender;
    private String Password;
    private String PhoneNumeber;
    private String Long;
    private String Lat;



    public Person(
        int ID,        String InsuranceNumber,        String Email,        String Balance,        String Image,        String Ssn,        String Last_Seen,        String Name,        int Gender,        String Password,        String PhoneNumeber,        String Long,        String Lat    ) {
        this.ID = ID;
        this.InsuranceNumber = InsuranceNumber;
        this.Email = Email;
        this.Balance = Balance;
        this.Image = Image;
        this.Ssn = Ssn;
        this.Last_Seen = Last_Seen;
        this.Name = Name;
        this.Gender = Gender;
        this.Password = Password;
        this.PhoneNumeber = PhoneNumeber;
        this.Long = Long;
        this.Lat = Lat;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getInsurancenumber() {
        return InsuranceNumber;
    }

    public void setInsurancenumber(String InsuranceNumber) {
        this.InsuranceNumber = InsuranceNumber;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
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
    public String getSsn() {
        return Ssn;
    }

    public void setSsn(String Ssn) {
        this.Ssn = Ssn;
    }
    public String getLast_seen() {
        return Last_Seen;
    }

    public void setLast_seen(String Last_Seen) {
        this.Last_Seen = Last_Seen;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getGender() {
        return Gender;
    }

    public void setGender(int Gender) {
        this.Gender = Gender;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getPhonenumeber() {
        return PhoneNumeber;
    }

    public void setPhonenumeber(String PhoneNumeber) {
        this.PhoneNumeber = PhoneNumeber;
    }
    public String getLong() {
        return Long;
    }

    public void setLong(String Long) {
        this.Long = Long;
    }
    public String getLat() {
        return Lat;
    }

    public void setLat(String Lat) {
        this.Lat = Lat;
    }


}