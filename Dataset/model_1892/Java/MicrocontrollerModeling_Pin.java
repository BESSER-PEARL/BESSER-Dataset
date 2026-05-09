





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_Pin  {

    private int number;
    private String nature;
    private String name;





    private MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller;


    public MicrocontrollerModeling_Pin(
        int number,        String nature,        String name    ) {
        this.number = number;
        this.nature = nature;
        this.name = name;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MicrocontrollerModeling_Microcontroller getMicrocontrollermodeling_microcontroller() {
        return microcontrollermodeling_microcontroller;
    }

    public void setMicrocontrollermodeling_microcontroller(MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller) {
        this.microcontrollermodeling_microcontroller = microcontrollermodeling_microcontroller;
    }

}