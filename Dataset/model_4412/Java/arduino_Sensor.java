





import java.util.List;
import java.util.ArrayList;

public class arduino_Sensor extends BooleanOperator, ModuleInstruction {






    private arduino_Status arduino_status;




    private List<arduino_Status> arduino_statuss;


    public arduino_Sensor(
    ) {
        super(
        );
        this.arduino_statuss = new ArrayList<>();
    }

    public arduino_Sensor(
        ArrayList<arduino_Status> arduino_statuss    ) {
        this.arduino_statuss = arduino_statuss;
    }


    public arduino_Status getArduino_status() {
        return arduino_status;
    }

    public void setArduino_status(arduino_Status arduino_status) {
        this.arduino_status = arduino_status;
    }
    public List<arduino_Status> getArduino_statuss() {
        return arduino_statuss;
    }

    public void addArduino_status(Arduino_status arduino_status) {
        this.arduino_statuss.add(arduino_status);
    }

}