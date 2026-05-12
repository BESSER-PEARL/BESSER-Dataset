





import java.util.List;
import java.util.ArrayList;

public class Airport  {

    private String Address;
    private String AirportID;
    private String AirportName;





    private List<Routes> routess;


    public Airport(
        String Address,        String AirportID,        String AirportName    ) {
        this.Address = Address;
        this.AirportID = AirportID;
        this.AirportName = AirportName;
        this.routess = new ArrayList<>();
    }

    public Airport(
        String Address,        String AirportID,        String AirportName        ArrayList<Routes> routess    ) {
        this.Address = Address;
        this.AirportID = AirportID;
        this.AirportName = AirportName;
        this.routess = routess;
    }

    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
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

    public List<Routes> getRoutess() {
        return routess;
    }

    public void addRoutes(Routes routes) {
        this.routess.add(routes);
    }

}