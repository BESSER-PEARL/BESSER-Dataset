





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_Processor  {

    private int speed;
    private String unit;





    private MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller;


    public MicrocontrollerModeling_Processor(
        int speed,        String unit    ) {
        this.speed = speed;
        this.unit = unit;
    }


    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public MicrocontrollerModeling_Microcontroller getMicrocontrollermodeling_microcontroller() {
        return microcontrollermodeling_microcontroller;
    }

    public void setMicrocontrollermodeling_microcontroller(MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller) {
        this.microcontrollermodeling_microcontroller = microcontrollermodeling_microcontroller;
    }

}