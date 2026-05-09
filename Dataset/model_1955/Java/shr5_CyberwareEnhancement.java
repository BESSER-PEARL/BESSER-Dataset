





import java.util.List;
import java.util.ArrayList;

public class shr5_CyberwareEnhancement extends AbstraktModifikatoren, GeldWert {

    private String type;
    private int capacityUse;



    public shr5_CyberwareEnhancement(
        String type,        int capacityUse    ) {
        super(
        );
        this.type = type;
        this.capacityUse = capacityUse;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getCapacityuse() {
        return capacityUse;
    }

    public void setCapacityuse(int capacityUse) {
        this.capacityUse = capacityUse;
    }


}