





import java.util.List;
import java.util.ArrayList;

public class bank_Phone extends ContactMethod {

    private int extension;
    private int phoneNumber;
    private int areaCode;
    private int countryCode;



    public bank_Phone(
        int extension,        int phoneNumber,        int areaCode,        int countryCode    ) {
        super(
        );
        this.extension = extension;
        this.phoneNumber = phoneNumber;
        this.areaCode = areaCode;
        this.countryCode = countryCode;
    }


    public int getExtension() {
        return extension;
    }

    public void setExtension(int extension) {
        this.extension = extension;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public int getAreacode() {
        return areaCode;
    }

    public void setAreacode(int areaCode) {
        this.areaCode = areaCode;
    }
    public int getCountrycode() {
        return countryCode;
    }

    public void setCountrycode(int countryCode) {
        this.countryCode = countryCode;
    }


}