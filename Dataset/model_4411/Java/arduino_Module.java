





import java.util.List;
import java.util.ArrayList;

public class arduino_Module extends NamedElement {

    private String kind;
    private String library;
    private boolean level;
    private String image;





    private arduino_Hardware arduino_hardware;


    public arduino_Module(
        String kind,        String library,        boolean level,        String image    ) {
        super(
        );
        this.kind = kind;
        this.library = library;
        this.level = level;
        this.image = image;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getLibrary() {
        return library;
    }

    public void setLibrary(String library) {
        this.library = library;
    }
    public boolean getLevel() {
        return level;
    }

    public void setLevel(boolean level) {
        this.level = level;
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