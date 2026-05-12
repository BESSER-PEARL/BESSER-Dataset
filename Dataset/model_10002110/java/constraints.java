





import java.util.List;
import java.util.ArrayList;

public class constraints  {

    private None doubletons;
    private None singletons;



    public constraints(
        None doubletons,        None singletons    ) {
        this.doubletons = doubletons;
        this.singletons = singletons;
    }


    public None getDoubletons() {
        return doubletons;
    }

    public void setDoubletons(None doubletons) {
        this.doubletons = doubletons;
    }
    public None getSingletons() {
        return singletons;
    }

    public void setSingletons(None singletons) {
        this.singletons = singletons;
    }


}