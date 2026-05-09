





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_City  {

    private String name;
    private int id;
    private String abbr;





    private List<reservationsystem_Airport> reservationsystem_airports;




    private reservationsystem_Airport reservationsystem_airport;


    public reservationsystem_City(
        String name,        int id,        String abbr    ) {
        this.name = name;
        this.id = id;
        this.abbr = abbr;
        this.reservationsystem_airports = new ArrayList<>();
    }

    public reservationsystem_City(
        String name,        int id,        String abbr        ArrayList<reservationsystem_Airport> reservationsystem_airports    ) {
        this.name = name;
        this.id = id;
        this.abbr = abbr;
        this.reservationsystem_airports = reservationsystem_airports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAbbr() {
        return abbr;
    }

    public void setAbbr(String abbr) {
        this.abbr = abbr;
    }

    public List<reservationsystem_Airport> getReservationsystem_airports() {
        return reservationsystem_airports;
    }

    public void addReservationsystem_airport(Reservationsystem_airport reservationsystem_airport) {
        this.reservationsystem_airports.add(reservationsystem_airport);
    }
    public reservationsystem_Airport getReservationsystem_airport() {
        return reservationsystem_airport;
    }

    public void setReservationsystem_airport(reservationsystem_Airport reservationsystem_airport) {
        this.reservationsystem_airport = reservationsystem_airport;
    }

}