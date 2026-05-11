





import java.util.List;
import java.util.ArrayList;

public class MARTE_GCM_FlowPort  {

    private String direction;
    private String isConjugated;
    private String isAtomic;



    public MARTE_GCM_FlowPort(
        String direction,        String isConjugated,        String isAtomic    ) {
        this.direction = direction;
        this.isConjugated = isConjugated;
        this.isAtomic = isAtomic;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getIsconjugated() {
        return isConjugated;
    }

    public void setIsconjugated(String isConjugated) {
        this.isConjugated = isConjugated;
    }
    public String getIsatomic() {
        return isAtomic;
    }

    public void setIsatomic(String isAtomic) {
        this.isAtomic = isAtomic;
    }


}