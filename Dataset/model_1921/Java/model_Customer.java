





import java.util.List;
import java.util.ArrayList;

public class model_Customer  {

    private String expiringYear;
    private String ccNumber;
    private String expiringMonth;
    private String firstName;
    private String ccv;
    private String email;
    private String adress;
    private String surname;



    public model_Customer(
        String expiringYear,        String ccNumber,        String expiringMonth,        String firstName,        String ccv,        String email,        String adress,        String surname    ) {
        this.expiringYear = expiringYear;
        this.ccNumber = ccNumber;
        this.expiringMonth = expiringMonth;
        this.firstName = firstName;
        this.ccv = ccv;
        this.email = email;
        this.adress = adress;
        this.surname = surname;
    }


    public String getExpiringyear() {
        return expiringYear;
    }

    public void setExpiringyear(String expiringYear) {
        this.expiringYear = expiringYear;
    }
    public String getCcnumber() {
        return ccNumber;
    }

    public void setCcnumber(String ccNumber) {
        this.ccNumber = ccNumber;
    }
    public String getExpiringmonth() {
        return expiringMonth;
    }

    public void setExpiringmonth(String expiringMonth) {
        this.expiringMonth = expiringMonth;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getCcv() {
        return ccv;
    }

    public void setCcv(String ccv) {
        this.ccv = ccv;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }


}