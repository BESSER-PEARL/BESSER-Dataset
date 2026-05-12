





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String State;
    private String City;
    private String Type;
    private String Street;
    private String Country;
    private String ZipCode;



    public Address(
        String State,        String City,        String Type,        String Street,        String Country,        String ZipCode    ) {
        this.State = State;
        this.City = City;
        this.Type = Type;
        this.Street = Street;
        this.Country = Country;
        this.ZipCode = ZipCode;
    }


    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getStreet() {
        return Street;
    }

    public void setStreet(String Street) {
        this.Street = Street;
    }
    public String getCountry() {
        return Country;
    }

    public void setCountry(String Country) {
        this.Country = Country;
    }
    public String getZipcode() {
        return ZipCode;
    }

    public void setZipcode(String ZipCode) {
        this.ZipCode = ZipCode;
    }


}