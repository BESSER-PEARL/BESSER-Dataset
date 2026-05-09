





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_Memory  {

    private int size;
    private String unit;



    public MicrocontrollerModeling_Memory(
        int size,        String unit    ) {
        this.size = size;
        this.unit = unit;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}