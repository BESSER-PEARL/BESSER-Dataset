





import java.util.List;
import java.util.ArrayList;

public class Coach  {

    private int capacity;
    private int totalPassengers;
    private String humidity;
    private String temprature;
    private String coachType;



    public Coach(
        int capacity,        int totalPassengers,        String humidity,        String temprature,        String coachType    ) {
        this.capacity = capacity;
        this.totalPassengers = totalPassengers;
        this.humidity = humidity;
        this.temprature = temprature;
        this.coachType = coachType;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
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
    public String getTemprature() {
        return temprature;
    }

    public void setTemprature(String temprature) {
        this.temprature = temprature;
    }
    public String getCoachtype() {
        return coachType;
    }

    public void setCoachtype(String coachType) {
        this.coachType = coachType;
    }


}