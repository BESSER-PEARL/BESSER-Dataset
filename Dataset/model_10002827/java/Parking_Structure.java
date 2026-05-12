





import java.util.List;
import java.util.ArrayList;

public class Parking_Structure  {

    private String City;
    private None Type;
    private String Address;



    public Parking_Structure(
        String City,        None Type,        String Address    ) {
        this.City = City;
        this.Type = Type;
        this.Address = Address;
    }


    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public None getType() {
        return Type;
    }

    public void setType(None Type) {
        this.Type = Type;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}