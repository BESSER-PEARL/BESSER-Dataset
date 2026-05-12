





import java.util.List;
import java.util.ArrayList;

public class Coach  {

    private String humidity;
    private int capacity;
    private String temprature;
    private int totalPassengers;
    private String coachType;



    public Coach(
        String humidity,        int capacity,        String temprature,        int totalPassengers,        String coachType    ) {
        this.humidity = humidity;
        this.capacity = capacity;
        this.temprature = temprature;
        this.totalPassengers = totalPassengers;
        this.coachType = coachType;
    }


    public String getHumidity() {
        return humidity;
    }

    public void setHumidity(String humidity) {
        this.humidity = humidity;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getTemprature() {
        return temprature;
    }

    public void setTemprature(String temprature) {
        this.temprature = temprature;
    }
    public int getTotalpassengers() {
        return totalPassengers;
    }

    public void setTotalpassengers(int totalPassengers) {
        this.totalPassengers = totalPassengers;
    }
    public String getCoachtype() {
        return coachType;
    }

    public void setCoachtype(String coachType) {
        this.coachType = coachType;
    }


}