





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Airport  {

    private String abbr;
    private int id;
    private String name;





    private reservationsystem_GeneralFlight reservationsystem_generalflight;




    private reservationsystem_GeneralFlight reservationsystem_generalflight;


    public reservationsystem_Airport(
        String abbr,        int id,        String name    ) {
        this.abbr = abbr;
        this.id = id;
        this.name = name;
    }


    public String getAbbr() {
        return abbr;
    }

    public void setAbbr(String abbr) {
        this.abbr = abbr;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public reservationsystem_GeneralFlight getReservationsystem_generalflight() {
        return reservationsystem_generalflight;
    }

    public void setReservationsystem_generalflight(reservationsystem_GeneralFlight reservationsystem_generalflight) {
        this.reservationsystem_generalflight = reservationsystem_generalflight;
    }
    public reservationsystem_GeneralFlight getReservationsystem_generalflight() {
        return reservationsystem_generalflight;
    }

    public void setReservationsystem_generalflight(reservationsystem_GeneralFlight reservationsystem_generalflight) {
        this.reservationsystem_generalflight = reservationsystem_generalflight;
    }

}