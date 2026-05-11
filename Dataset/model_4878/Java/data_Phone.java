





import java.util.List;
import java.util.ArrayList;

public class data_Phone extends MetaInformation {

    private String number;
    private String areaCode;
    private String countryCode;



    public data_Phone(
        String number,        String areaCode,        String countryCode    ) {
        super(
        );
        this.number = number;
        this.areaCode = areaCode;
        this.countryCode = countryCode;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getAreacode() {
        return areaCode;
    }

    public void setAreacode(String areaCode) {
        this.areaCode = areaCode;
    }
    public String getCountrycode() {
        return countryCode;
    }

    public void setCountrycode(String countryCode) {
        this.countryCode = countryCode;
    }


}