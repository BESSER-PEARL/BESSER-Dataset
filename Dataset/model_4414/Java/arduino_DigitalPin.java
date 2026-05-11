





import java.util.List;
import java.util.ArrayList;

public class arduino_DigitalPin extends Pin {

    private String number;





    private arduino_Setup arduino_setup;




    private arduino_Read arduino_read;




    private arduino_Write arduino_write;


    public arduino_DigitalPin(
        String number    ) {
        super(
        );
        this.number = number;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public arduino_Setup getArduino_setup() {
        return arduino_setup;
    }

    public void setArduino_setup(arduino_Setup arduino_setup) {
        this.arduino_setup = arduino_setup;
    }
    public arduino_Read getArduino_read() {
        return arduino_read;
    }

    public void setArduino_read(arduino_Read arduino_read) {
        this.arduino_read = arduino_read;
    }
    public arduino_Write getArduino_write() {
        return arduino_write;
    }

    public void setArduino_write(arduino_Write arduino_write) {
        this.arduino_write = arduino_write;
    }

}