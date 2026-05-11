





import java.util.List;
import java.util.ArrayList;

public class arduino_Poll  {

    private int h;
    private int l;
    private String type;





    private arduino_Sketch arduino_sketch;




    private arduino_Handler arduino_handler;


    public arduino_Poll(
        int h,        int l,        String type    ) {
        this.h = h;
        this.l = l;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }
    public arduino_Handler getArduino_handler() {
        return arduino_handler;
    }

    public void setArduino_handler(arduino_Handler arduino_handler) {
        this.arduino_handler = arduino_handler;
    }

}