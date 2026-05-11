





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwROM extends HwMemory {

    private String organization;
    private String type;



    public MARTE_HwMemory_HwROM(
        String organization,        String type    ) {
        super(
        );
        this.organization = organization;
        this.type = type;
    }


    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}