





import java.util.List;
import java.util.ArrayList;

public class marsRover_avoid_obstacles  {

    private String name;





    private List<marsRover_EObject> marsrover_eobjects;


    public marsRover_avoid_obstacles(
        String name    ) {
        this.name = name;
        this.marsrover_eobjects = new ArrayList<>();
    }

    public marsRover_avoid_obstacles(
        String name        ArrayList<marsRover_EObject> marsrover_eobjects    ) {
        this.name = name;
        this.marsrover_eobjects = marsrover_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<marsRover_EObject> getMarsrover_eobjects() {
        return marsrover_eobjects;
    }

    public void addMarsrover_eobject(Marsrover_eobject marsrover_eobject) {
        this.marsrover_eobjects.add(marsrover_eobject);
    }

}