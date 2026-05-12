




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class FlightSystem_Flight  {

    private int _miles;
    private int _duration;
    private None flightType;
    private LocalDate schedule;
    private None airportTo;
    private None airportFrom;





    private Company_Company company_company;


    public FlightSystem_Flight(
        int _miles,        int _duration,        None flightType,        LocalDate schedule,        None airportTo,        None airportFrom    ) {
        this._miles = _miles;
        this._duration = _duration;
        this.flightType = flightType;
        this.schedule = schedule;
        this.airportTo = airportTo;
        this.airportFrom = airportFrom;
    }


    public int get_miles() {
        return _miles;
    }

    public void set_miles(int _miles) {
        this._miles = _miles;
    }
    public int get_duration() {
        return _duration;
    }

    public void set_duration(int _duration) {
        this._duration = _duration;
    }
    public None getFlighttype() {
        return flightType;
    }

    public void setFlighttype(None flightType) {
        this.flightType = flightType;
    }
    public LocalDate getSchedule() {
        return schedule;
    }

    public void setSchedule(LocalDate schedule) {
        this.schedule = schedule;
    }
    public None getAirportto() {
        return airportTo;
    }

    public void setAirportto(None airportTo) {
        this.airportTo = airportTo;
    }
    public None getAirportfrom() {
        return airportFrom;
    }

    public void setAirportfrom(None airportFrom) {
        this.airportFrom = airportFrom;
    }

    public Company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(Company_Company company_company) {
        this.company_company = company_company;
    }

}