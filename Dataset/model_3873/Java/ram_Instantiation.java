





import java.util.List;
import java.util.ArrayList;

public class ram_Instantiation  {

    private String type;





    private ram_Aspect ram_aspect;


    public ram_Instantiation(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ram_Aspect getRam_aspect() {
        return ram_aspect;
    }

    public void setRam_aspect(ram_Aspect ram_aspect) {
        this.ram_aspect = ram_aspect;
    }

}