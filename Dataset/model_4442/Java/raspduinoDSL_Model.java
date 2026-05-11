





import java.util.List;
import java.util.ArrayList;

public class raspduinoDSL_Model  {

    private String name;
    private String hardware;



    public raspduinoDSL_Model(
        String name,        String hardware    ) {
        this.name = name;
        this.hardware = hardware;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHardware() {
        return hardware;
    }

    public void setHardware(String hardware) {
        this.hardware = hardware;
    }


}