





import java.util.List;
import java.util.ArrayList;

public class moba_MobaGeneratorSlot extends MobaApplicationFeature {

    private String type;
    private String name;





    private moba_MobaGeneratorSlot moba_mobageneratorslot;


    public moba_MobaGeneratorSlot(
        String type,        String name    ) {
        super(
        );
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public moba_MobaGeneratorSlot getMoba_mobageneratorslot() {
        return moba_mobageneratorslot;
    }

    public void setMoba_mobageneratorslot(moba_MobaGeneratorSlot moba_mobageneratorslot) {
        this.moba_mobageneratorslot = moba_mobageneratorslot;
    }

}