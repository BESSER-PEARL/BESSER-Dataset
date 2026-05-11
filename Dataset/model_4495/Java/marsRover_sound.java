





import java.util.List;
import java.util.ArrayList;

public class marsRover_sound  {

    private String name;
    private int duration;
    private int frequency;



    public marsRover_sound(
        String name,        int duration,        int frequency    ) {
        this.name = name;
        this.duration = duration;
        this.frequency = frequency;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getFrequency() {
        return frequency;
    }

    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }


}