





import java.util.List;
import java.util.ArrayList;

public class Cleaning_Management  {

    private String brushing;
    private String water;
    private String powderized_wash;





    private User user;


    public Cleaning_Management(
        String brushing,        String water,        String powderized_wash    ) {
        this.brushing = brushing;
        this.water = water;
        this.powderized_wash = powderized_wash;
    }


    public String getBrushing() {
        return brushing;
    }

    public void setBrushing(String brushing) {
        this.brushing = brushing;
    }
    public String getWater() {
        return water;
    }

    public void setWater(String water) {
        this.water = water;
    }
    public String getPowderized_wash() {
        return powderized_wash;
    }

    public void setPowderized_wash(String powderized_wash) {
        this.powderized_wash = powderized_wash;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}