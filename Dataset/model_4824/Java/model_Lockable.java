





import java.util.List;
import java.util.ArrayList;

public class model_Lockable  {

    private boolean locked;



    public model_Lockable(
        boolean locked    ) {
        this.locked = locked;
    }


    public boolean getLocked() {
        return locked;
    }

    public void setLocked(boolean locked) {
        this.locked = locked;
    }


}