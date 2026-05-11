





import java.util.List;
import java.util.ArrayList;

public class iot2_HWComponent  {

    private boolean name;





    private iot2_System iot2_system;


    public iot2_HWComponent(
        boolean name    ) {
        this.name = name;
    }


    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
    }

    public iot2_System getIot2_system() {
        return iot2_system;
    }

    public void setIot2_system(iot2_System iot2_system) {
        this.iot2_system = iot2_system;
    }

}