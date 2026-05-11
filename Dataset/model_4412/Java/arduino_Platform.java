





import java.util.List;
import java.util.ArrayList;

public class arduino_Platform extends NamedElement {

    private String image;





    private arduino_Hardware arduino_hardware;




    private List<arduino_DigitalPin> arduino_digitalpins;




    private arduino_Project arduino_project;




    private List<arduino_AnalogPin> arduino_analogpins;


    public arduino_Platform(
        String image    ) {
        super(
        );
        this.image = image;
        this.arduino_digitalpins = new ArrayList<>();
        this.arduino_analogpins = new ArrayList<>();
    }

    public arduino_Platform(
        String image        ArrayList<arduino_DigitalPin> arduino_digitalpins,        ArrayList<arduino_AnalogPin> arduino_analogpins    ) {
        this.image = image;
        this.arduino_digitalpins = arduino_digitalpins;
        this.arduino_analogpins = arduino_analogpins;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public arduino_Hardware getArduino_hardware() {
        return arduino_hardware;
    }

    public void setArduino_hardware(arduino_Hardware arduino_hardware) {
        this.arduino_hardware = arduino_hardware;
    }
    public List<arduino_DigitalPin> getArduino_digitalpins() {
        return arduino_digitalpins;
    }

    public void addArduino_digitalpin(Arduino_digitalpin arduino_digitalpin) {
        this.arduino_digitalpins.add(arduino_digitalpin);
    }
    public arduino_Project getArduino_project() {
        return arduino_project;
    }

    public void setArduino_project(arduino_Project arduino_project) {
        this.arduino_project = arduino_project;
    }
    public List<arduino_AnalogPin> getArduino_analogpins() {
        return arduino_analogpins;
    }

    public void addArduino_analogpin(Arduino_analogpin arduino_analogpin) {
        this.arduino_analogpins.add(arduino_analogpin);
    }

}