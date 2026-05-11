





import java.util.List;
import java.util.ArrayList;

public class MARTE_GCM_FlowPort  {

    private String direction;
    private String isAtomic;



    public MARTE_GCM_FlowPort(
        String direction,        String isAtomic    ) {
        this.direction = direction;
        this.isAtomic = isAtomic;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getIsatomic() {
        return isAtomic;
    }

    public void setIsatomic(String isAtomic) {
        this.isAtomic = isAtomic;
    }


}