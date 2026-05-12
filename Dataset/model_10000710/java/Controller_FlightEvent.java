




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Controller_FlightEvent  {

    private LocalDate _dateBegin;
    private String _title;
    private LocalDate _dateEnd;
    private None flight;



    public Controller_FlightEvent(
        LocalDate _dateBegin,        String _title,        LocalDate _dateEnd,        None flight    ) {
        this._dateBegin = _dateBegin;
        this._title = _title;
        this._dateEnd = _dateEnd;
        this.flight = flight;
    }


    public LocalDate get_datebegin() {
        return _dateBegin;
    }

    public void set_datebegin(LocalDate _dateBegin) {
        this._dateBegin = _dateBegin;
    }
    public String get_title() {
        return _title;
    }

    public void set_title(String _title) {
        this._title = _title;
    }
    public LocalDate get_dateend() {
        return _dateEnd;
    }

    public void set_dateend(LocalDate _dateEnd) {
        this._dateEnd = _dateEnd;
    }
    public None getFlight() {
        return flight;
    }

    public void setFlight(None flight) {
        this.flight = flight;
    }


}