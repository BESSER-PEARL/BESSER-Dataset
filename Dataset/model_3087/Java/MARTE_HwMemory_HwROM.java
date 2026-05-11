





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwROM extends HwMemory {

    private String type;



    public MARTE_HwMemory_HwROM(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}