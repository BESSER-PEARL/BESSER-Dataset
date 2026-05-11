





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Brick  {

    private int pin;
    private String name;





    private arduinoml_Board arduinoml_board;


    public arduinoml_Brick(
        int pin,        String name    ) {
        this.pin = pin;
        this.name = name;
    }


    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduinoml_Board getArduinoml_board() {
        return arduinoml_board;
    }

    public void setArduinoml_board(arduinoml_Board arduinoml_board) {
        this.arduinoml_board = arduinoml_board;
    }

}