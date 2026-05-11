





import java.util.List;
import java.util.ArrayList;

public class iot_Motor  {

    private int pins;
    private String name;
    private String degrees;
    private String library;





    private iot_Arduino iot_arduino;




    private iot_Motor iot_motor;




    private iot_Board iot_board;


    public iot_Motor(
        int pins,        String name,        String degrees,        String library    ) {
        this.pins = pins;
        this.name = name;
        this.degrees = degrees;
        this.library = library;
    }


    public int getPins() {
        return pins;
    }

    public void setPins(int pins) {
        this.pins = pins;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDegrees() {
        return degrees;
    }

    public void setDegrees(String degrees) {
        this.degrees = degrees;
    }
    public String getLibrary() {
        return library;
    }

    public void setLibrary(String library) {
        this.library = library;
    }

    public iot_Arduino getIot_arduino() {
        return iot_arduino;
    }

    public void setIot_arduino(iot_Arduino iot_arduino) {
        this.iot_arduino = iot_arduino;
    }
    public iot_Motor getIot_motor() {
        return iot_motor;
    }

    public void setIot_motor(iot_Motor iot_motor) {
        this.iot_motor = iot_motor;
    }
    public iot_Board getIot_board() {
        return iot_board;
    }

    public void setIot_board(iot_Board iot_board) {
        this.iot_board = iot_board;
    }

}