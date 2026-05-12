





import java.util.List;
import java.util.ArrayList;

public class Grafcet_Step extends Element {

    private String isActive;
    private String action;
    private String isInitial;



    public Grafcet_Step(
        String isActive,        String action,        String isInitial    ) {
        super(
        );
        this.isActive = isActive;
        this.action = action;
        this.isInitial = isInitial;
    }


    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(String isInitial) {
        this.isInitial = isInitial;
    }


}