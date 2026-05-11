





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_ZipCode  {

    private String number;
    private String extension;
    private String country;



    public org_aries_common_ZipCode(
        String number,        String extension,        String country    ) {
        this.number = number;
        this.extension = extension;
        this.country = country;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }


}