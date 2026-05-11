





import java.util.List;
import java.util.ArrayList;

public class tExp_Singletons extends Constraint {

    private int maxSingletons;
    private int minSingletons;



    public tExp_Singletons(
        int maxSingletons,        int minSingletons    ) {
        super(
        );
        this.maxSingletons = maxSingletons;
        this.minSingletons = minSingletons;
    }


    public int getMaxsingletons() {
        return maxSingletons;
    }

    public void setMaxsingletons(int maxSingletons) {
        this.maxSingletons = maxSingletons;
    }
    public int getMinsingletons() {
        return minSingletons;
    }

    public void setMinsingletons(int minSingletons) {
        this.minSingletons = minSingletons;
    }


}