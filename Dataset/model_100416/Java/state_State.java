





import java.util.List;
import java.util.ArrayList;

public class state_State extends Node {

    private String duration;
    private String name;



    public state_State(
        String duration,        String name    ) {
        super(
        );
        this.duration = duration;
        this.name = name;
    }


    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}