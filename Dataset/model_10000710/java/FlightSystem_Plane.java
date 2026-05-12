





import java.util.List;
import java.util.ArrayList;

public class FlightSystem_Plane  {

    private int _flySinceRefuel;
    private None _location;
    private int nbPilote;
    private None _crew;
    private None _state;
    private int seatPerRow;
    private int nbSteward;
    private int row;
    private int _millesFlyed;
    private int _seat;
    private int _millesSinceRevisionned;





    private ProviderSystem_ConsomationStock providersystem_consomationstock;




    private List<FlightSystem_Flight> flightsystem_flights;




    private Company_Company company_company;


    public FlightSystem_Plane(
        int _flySinceRefuel,        None _location,        int nbPilote,        None _crew,        None _state,        int seatPerRow,        int nbSteward,        int row,        int _millesFlyed,        int _seat,        int _millesSinceRevisionned    ) {
        this._flySinceRefuel = _flySinceRefuel;
        this._location = _location;
        this.nbPilote = nbPilote;
        this._crew = _crew;
        this._state = _state;
        this.seatPerRow = seatPerRow;
        this.nbSteward = nbSteward;
        this.row = row;
        this._millesFlyed = _millesFlyed;
        this._seat = _seat;
        this._millesSinceRevisionned = _millesSinceRevisionned;
        this.flightsystem_flights = new ArrayList<>();
    }

    public FlightSystem_Plane(
        int _flySinceRefuel,        None _location,        int nbPilote,        None _crew,        None _state,        int seatPerRow,        int nbSteward,        int row,        int _millesFlyed,        int _seat,        int _millesSinceRevisionned        ArrayList<FlightSystem_Flight> flightsystem_flights    ) {
        this._flySinceRefuel = _flySinceRefuel;
        this._location = _location;
        this.nbPilote = nbPilote;
        this._crew = _crew;
        this._state = _state;
        this.seatPerRow = seatPerRow;
        this.nbSteward = nbSteward;
        this.row = row;
        this._millesFlyed = _millesFlyed;
        this._seat = _seat;
        this._millesSinceRevisionned = _millesSinceRevisionned;
        this.flightsystem_flights = flightsystem_flights;
    }

    public int get_flysincerefuel() {
        return _flySinceRefuel;
    }

    public void set_flysincerefuel(int _flySinceRefuel) {
        this._flySinceRefuel = _flySinceRefuel;
    }
    public None get_location() {
        return _location;
    }

    public void set_location(None _location) {
        this._location = _location;
    }
    public int getNbpilote() {
        return nbPilote;
    }

    public void setNbpilote(int nbPilote) {
        this.nbPilote = nbPilote;
    }
    public None get_crew() {
        return _crew;
    }

    public void set_crew(None _crew) {
        this._crew = _crew;
    }
    public None get_state() {
        return _state;
    }

    public void set_state(None _state) {
        this._state = _state;
    }
    public int getSeatperrow() {
        return seatPerRow;
    }

    public void setSeatperrow(int seatPerRow) {
        this.seatPerRow = seatPerRow;
    }
    public int getNbsteward() {
        return nbSteward;
    }

    public void setNbsteward(int nbSteward) {
        this.nbSteward = nbSteward;
    }
    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }
    public int get_millesflyed() {
        return _millesFlyed;
    }

    public void set_millesflyed(int _millesFlyed) {
        this._millesFlyed = _millesFlyed;
    }
    public int get_seat() {
        return _seat;
    }

    public void set_seat(int _seat) {
        this._seat = _seat;
    }
    public int get_millessincerevisionned() {
        return _millesSinceRevisionned;
    }

    public void set_millessincerevisionned(int _millesSinceRevisionned) {
        this._millesSinceRevisionned = _millesSinceRevisionned;
    }

    public ProviderSystem_ConsomationStock getProvidersystem_consomationstock() {
        return providersystem_consomationstock;
    }

    public void setProvidersystem_consomationstock(ProviderSystem_ConsomationStock providersystem_consomationstock) {
        this.providersystem_consomationstock = providersystem_consomationstock;
    }
    public List<FlightSystem_Flight> getFlightsystem_flights() {
        return flightsystem_flights;
    }

    public void addFlightsystem_flight(Flightsystem_flight flightsystem_flight) {
        this.flightsystem_flights.add(flightsystem_flight);
    }
    public Company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(Company_Company company_company) {
        this.company_company = company_company;
    }

}