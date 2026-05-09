





import java.util.List;
import java.util.ArrayList;

public class shr5_Drohne extends MatrixAttributes, Fahrzeug {

    private int programSlotCount;



    public shr5_Drohne(
        int programSlotCount    ) {
        super(
        );
        this.programSlotCount = programSlotCount;
    }


    public int getProgramslotcount() {
        return programSlotCount;
    }

    public void setProgramslotcount(int programSlotCount) {
        this.programSlotCount = programSlotCount;
    }


}