





import java.util.List;
import java.util.ArrayList;

public class complworld_Thing  {

    private String name;





    private complworld_World complworld_world;


    public complworld_Thing(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public complworld_World getComplworld_world() {
        return complworld_world;
    }

    public void setComplworld_world(complworld_World complworld_world) {
        this.complworld_world = complworld_world;
    }

}