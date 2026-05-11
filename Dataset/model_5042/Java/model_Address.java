





import java.util.List;
import java.util.ArrayList;

public class model_Address extends IEntity {

    private String countryCode;
    private String manualAddress;
    private String city;
    private String cityAddon;
    private String street;
    private String zip;



    public model_Address(
        String countryCode,        String manualAddress,        String city,        String cityAddon,        String street,        String zip    ) {
        super(
        );
        this.countryCode = countryCode;
        this.manualAddress = manualAddress;
        this.city = city;
        this.cityAddon = cityAddon;
        this.street = street;
        this.zip = zip;
    }


    public String getCountrycode() {
        return countryCode;
    }

    public void setCountrycode(String countryCode) {
        this.countryCode = countryCode;
    }
    public String getManualaddress() {
        return manualAddress;
    }

    public void setManualaddress(String manualAddress) {
        this.manualAddress = manualAddress;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getCityaddon() {
        return cityAddon;
    }

    public void setCityaddon(String cityAddon) {
        this.cityAddon = cityAddon;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }


}