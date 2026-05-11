





import java.util.List;
import java.util.ArrayList;

public class trip_model_Service  {

    private String Type;
    private float Cost;
    private int Duration;
    private int Rating;
    private String name;



    public trip_model_Service(
        String Type,        float Cost,        int Duration,        int Rating,        String name    ) {
        this.Type = Type;
        this.Cost = Cost;
        this.Duration = Duration;
        this.Rating = Rating;
        this.name = name;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public float getCost() {
        return Cost;
    }

    public void setCost(float Cost) {
        this.Cost = Cost;
    }
    public int getDuration() {
        return Duration;
    }

    public void setDuration(int Duration) {
        this.Duration = Duration;
    }
    public int getRating() {
        return Rating;
    }

    public void setRating(int Rating) {
        this.Rating = Rating;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}