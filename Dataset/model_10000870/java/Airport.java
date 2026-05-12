





import java.util.List;
import java.util.ArrayList;

public class Airport  {

    private String AirportID;
    private String AirportName;
    private String Address;





    private List<Routes> routess;


    public Airport(
        String AirportID,        String AirportName,        String Address    ) {
        this.AirportID = AirportID;
        this.AirportName = AirportName;
        this.Address = Address;
        this.routess = new ArrayList<>();
    }

    public Airport(
        String AirportID,        String AirportName,        String Address        ArrayList<Routes> routess    ) {
        this.AirportID = AirportID;
        this.AirportName = AirportName;
        this.Address = Address;
        this.routess = routess;
    }

    public String getAirportid() {
        return AirportID;
    }

    public void setAirportid(String AirportID) {
        this.AirportID = AirportID;
    }
    public String getAirportname() {
        return AirportName;
    }

    public void setAirportname(String AirportName) {
        this.AirportName = AirportName;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public List<Routes> getRoutess() {
        return routess;
    }

    public void addRoutes(Routes routes) {
        this.routess.add(routes);
    }

}