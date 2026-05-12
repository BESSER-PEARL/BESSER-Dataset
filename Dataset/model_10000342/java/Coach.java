





import java.util.List;
import java.util.ArrayList;

public class Coach  {

    private String temprature;
    private int capacity;
    private String coachType;
    private int totalPassengers;
    private String humidity;



    public Coach(
        String temprature,        int capacity,        String coachType,        int totalPassengers,        String humidity    ) {
        this.temprature = temprature;
        this.capacity = capacity;
        this.coachType = coachType;
        this.totalPassengers = totalPassengers;
        this.humidity = humidity;
    }


    public String getTemprature() {
        return temprature;
    }

    public void setTemprature(String temprature) {
        this.temprature = temprature;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getCoachtype() {
        return coachType;
    }

    public void setCoachtype(String coachType) {
        this.coachType = coachType;
    }
    public int getTotalpassengers() {
        return totalPassengers;
    }

    public void setTotalpassengers(int totalPassengers) {
        this.totalPassengers = totalPassengers;
    }
    public String getHumidity() {
        return humidity;
    }

    public void setHumidity(String humidity) {
        this.humidity = humidity;
    }


}