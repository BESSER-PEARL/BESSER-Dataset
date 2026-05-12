





import java.util.List;
import java.util.ArrayList;

public class Display  {






    private List<System> systems;


    public Display(
    ) {
        this.systems = new ArrayList<>();
    }

    public Display(
        ArrayList<System> systems    ) {
        this.systems = systems;
    }


    public List<System> getSystems() {
        return systems;
    }

    public void addSystem(System system) {
        this.systems.add(system);
    }

}