





import java.util.List;
import java.util.ArrayList;

public class component_ExecutionContext extends WrapperObject, IPropertyMap {

    private int stateL;
    private int kindL;
    private String rateL;



    public component_ExecutionContext(
        int stateL,        int kindL,        String rateL    ) {
        super(
        );
        this.stateL = stateL;
        this.kindL = kindL;
        this.rateL = rateL;
    }


    public int getStatel() {
        return stateL;
    }

    public void setStatel(int stateL) {
        this.stateL = stateL;
    }
    public int getKindl() {
        return kindL;
    }

    public void setKindl(int kindL) {
        this.kindL = kindL;
    }
    public String getRatel() {
        return rateL;
    }

    public void setRatel(String rateL) {
        this.rateL = rateL;
    }


}