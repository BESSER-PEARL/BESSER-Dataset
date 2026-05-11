





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxArchetype extends DPrimitive {

    private String baseType;



    public dmx_DmxArchetype(
        String baseType    ) {
        super(
        );
        this.baseType = baseType;
    }


    public String getBasetype() {
        return baseType;
    }

    public void setBasetype(String baseType) {
        this.baseType = baseType;
    }


}