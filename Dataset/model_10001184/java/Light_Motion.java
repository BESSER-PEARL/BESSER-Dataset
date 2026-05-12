





import java.util.List;
import java.util.ArrayList;

public class Light_Motion  {

    private boolean Detects_Obstruction;



    public Light_Motion(
        boolean Detects_Obstruction    ) {
        this.Detects_Obstruction = Detects_Obstruction;
    }


    public boolean getDetects_obstruction() {
        return Detects_Obstruction;
    }

    public void setDetects_obstruction(boolean Detects_Obstruction) {
        this.Detects_Obstruction = Detects_Obstruction;
    }


}