





import java.util.List;
import java.util.ArrayList;

public class arduino_Platform extends NamedElement {

    private String image;





    private arduino_Hardware arduino_hardware;


    public arduino_Platform(
        String image    ) {
        super(
        );
        this.image = image;
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

}