





import java.util.List;
import java.util.ArrayList;

public class party_Phone extends ContactInfo {

    private String countryCode;
    private int areaCode;
    private String number;



    public party_Phone(
        String countryCode,        int areaCode,        String number    ) {
        super(
        );
        this.countryCode = countryCode;
        this.areaCode = areaCode;
        this.number = number;
    }


    public String getCountrycode() {
        return countryCode;
    }

    public void setCountrycode(String countryCode) {
        this.countryCode = countryCode;
    }
    public int getAreacode() {
        return areaCode;
    }

    public void setAreacode(int areaCode) {
        this.areaCode = areaCode;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }


}