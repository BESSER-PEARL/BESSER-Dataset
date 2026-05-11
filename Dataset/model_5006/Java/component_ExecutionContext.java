





import java.util.List;
import java.util.ArrayList;

public class component_ExecutionContext extends IPropertyMap, WrapperObject {

    private int stateL;
    private String rateL;
    private int kindL;



    public component_ExecutionContext(
        int stateL,        String rateL,        int kindL    ) {
        super(
        );
        this.stateL = stateL;
        this.rateL = rateL;
        this.kindL = kindL;
    }


    public int getStatel() {
        return stateL;
    }

    public void setStatel(int stateL) {
        this.stateL = stateL;
    }
    public String getRatel() {
        return rateL;
    }

    public void setRatel(String rateL) {
        this.rateL = rateL;
    }
    public int getKindl() {
        return kindL;
    }

    public void setKindl(int kindL) {
        this.kindL = kindL;
    }


}