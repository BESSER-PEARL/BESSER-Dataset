





import java.util.List;
import java.util.ArrayList;

public class rtsc_Transition extends NamedElement {

    private int hitCount;



    public rtsc_Transition(
        int hitCount    ) {
        super(
        );
        this.hitCount = hitCount;
    }


    public int getHitcount() {
        return hitCount;
    }

    public void setHitcount(int hitCount) {
        this.hitCount = hitCount;
    }


}