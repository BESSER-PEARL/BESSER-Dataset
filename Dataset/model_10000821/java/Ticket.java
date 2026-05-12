





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private boolean isLastMinute;
    private String eventCountry;
    private String eventCity;



    public Ticket(
        boolean isLastMinute,        String eventCountry,        String eventCity    ) {
        this.isLastMinute = isLastMinute;
        this.eventCountry = eventCountry;
        this.eventCity = eventCity;
    }


    public boolean getIslastminute() {
        return isLastMinute;
    }

    public void setIslastminute(boolean isLastMinute) {
        this.isLastMinute = isLastMinute;
    }
    public String getEventcountry() {
        return eventCountry;
    }

    public void setEventcountry(String eventCountry) {
        this.eventCountry = eventCountry;
    }
    public String getEventcity() {
        return eventCity;
    }

    public void setEventcity(String eventCity) {
        this.eventCity = eventCity;
    }


}