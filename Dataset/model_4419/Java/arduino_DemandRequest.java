





import java.util.List;
import java.util.ArrayList;

public class arduino_DemandRequest extends OutOperation {






    private List<arduino_Task> arduino_tasks;


    public arduino_DemandRequest(
    ) {
        super(
        );
        this.arduino_tasks = new ArrayList<>();
    }

    public arduino_DemandRequest(
        ArrayList<arduino_Task> arduino_tasks    ) {
        this.arduino_tasks = arduino_tasks;
    }


    public List<arduino_Task> getArduino_tasks() {
        return arduino_tasks;
    }

    public void addArduino_task(Arduino_task arduino_task) {
        this.arduino_tasks.add(arduino_task);
    }

}