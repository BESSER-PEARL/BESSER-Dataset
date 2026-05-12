





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_RegularCandy  {

    private int selfCrushRange;
    private boolean selfCrush;



    public candyCrushPackage_RegularCandy(
        int selfCrushRange,        boolean selfCrush    ) {
        this.selfCrushRange = selfCrushRange;
        this.selfCrush = selfCrush;
    }


    public int getSelfcrushrange() {
        return selfCrushRange;
    }

    public void setSelfcrushrange(int selfCrushRange) {
        this.selfCrushRange = selfCrushRange;
    }
    public boolean getSelfcrush() {
        return selfCrush;
    }

    public void setSelfcrush(boolean selfCrush) {
        this.selfCrush = selfCrush;
    }


}