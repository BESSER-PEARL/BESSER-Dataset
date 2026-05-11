





import java.util.List;
import java.util.ArrayList;

public class arduino_Bench  {

    private String name;





    private List<arduino_Arduino> arduino_arduinos;


    public arduino_Bench(
        String name    ) {
        this.name = name;
        this.arduino_arduinos = new ArrayList<>();
    }

    public arduino_Bench(
        String name        ArrayList<arduino_Arduino> arduino_arduinos    ) {
        this.name = name;
        this.arduino_arduinos = arduino_arduinos;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<arduino_Arduino> getArduino_arduinos() {
        return arduino_arduinos;
    }

    public void addArduino_arduino(Arduino_arduino arduino_arduino) {
        this.arduino_arduinos.add(arduino_arduino);
    }

}