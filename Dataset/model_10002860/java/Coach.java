





import java.util.List;
import java.util.ArrayList;

public class Coach  {

    private String humidity;
    private int totalPassengers;
    private String coachType;
    private int capacity;
    private String temprature;



    public Coach(
        String humidity,        int totalPassengers,        String coachType,        int capacity,        String temprature    ) {
        this.humidity = humidity;
        this.totalPassengers = totalPassengers;
        this.coachType = coachType;
        this.capacity = capacity;
        this.temprature = temprature;
    }


    public String getHumidity() {
        return humidity;
    }

    public void setHumidity(String humidity) {
        this.humidity = humidity;
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


}