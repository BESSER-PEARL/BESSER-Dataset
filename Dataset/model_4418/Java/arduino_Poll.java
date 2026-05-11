





import java.util.List;
import java.util.ArrayList;

public class arduino_Poll  {

    private String type;
    private int h;
    private int l;





    private arduino_Handler arduino_handler;


    public arduino_Poll(
        String type,        int h,        int l    ) {
        this.type = type;
        this.h = h;
        this.l = l;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getH() {
        return h;
    }

    public void setH(int h) {
        this.h = h;
    }
    public int getL() {
        return l;
    }

    public void setL(int l) {
        this.l = l;
    }

    public arduino_Handler getArduino_handler() {
        return arduino_handler;
    }

    public void setArduino_handler(arduino_Handler arduino_handler) {
        this.arduino_handler = arduino_handler;
    }

}