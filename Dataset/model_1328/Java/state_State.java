





import java.util.List;
import java.util.ArrayList;

public class state_State extends Node {

    private String name;
    private String duration;



    public state_State(
        String name,        String duration    ) {
        super(
        );
        this.name = name;
        this.duration = duration;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }


}