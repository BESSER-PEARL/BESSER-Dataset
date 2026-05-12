





import java.util.List;
import java.util.ArrayList;

public class DistributionSystem_Ticket  {

    private None from;
    private None payment;
    private int _numberPlace;
    private int _price;
    private boolean isRegistered;





    private FlightSystem_Flight flightsystem_flight;


    public DistributionSystem_Ticket(
        None from,        None payment,        int _numberPlace,        int _price,        boolean isRegistered    ) {
        this.from = from;
        this.payment = payment;
        this._numberPlace = _numberPlace;
        this._price = _price;
        this.isRegistered = isRegistered;
    }


    public None getFrom() {
        return from;
    }

    public void setFrom(None from) {
        this.from = from;
    }
    public None getPayment() {
        return payment;
    }

    public void setPayment(None payment) {
        this.payment = payment;
    }
    public int get_numberplace() {
        return _numberPlace;
    }

    public void set_numberplace(int _numberPlace) {
        this._numberPlace = _numberPlace;
    }
    public int get_price() {
        return _price;
    }

    public void set_price(int _price) {
        this._price = _price;
    }
    public boolean getIsregistered() {
        return isRegistered;
    }

    public void setIsregistered(boolean isRegistered) {
        this.isRegistered = isRegistered;
    }

    public FlightSystem_Flight getFlightsystem_flight() {
        return flightsystem_flight;
    }

    public void setFlightsystem_flight(FlightSystem_Flight flightsystem_flight) {
        this.flightsystem_flight = flightsystem_flight;
    }

}