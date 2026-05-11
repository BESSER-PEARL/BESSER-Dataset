





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_OSRequirement extends OSOrImageRequirement {

    private String os;
    private boolean is64os;



    public camel_requirement_OSRequirement(
        String os,        boolean is64os    ) {
        super(
        );
        this.os = os;
        this.is64os = is64os;
    }


    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }
    public boolean getIs64os() {
        return is64os;
    }

    public void setIs64os(boolean is64os) {
        this.is64os = is64os;
    }


}