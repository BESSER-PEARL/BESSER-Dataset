





import java.util.List;
import java.util.ArrayList;

public class model_base_IRecycled  {

    private boolean hasRecycledChildren;
    private boolean recycled;



    public model_base_IRecycled(
        boolean hasRecycledChildren,        boolean recycled    ) {
        this.hasRecycledChildren = hasRecycledChildren;
        this.recycled = recycled;
    }


    public boolean getHasrecycledchildren() {
        return hasRecycledChildren;
    }

    public void setHasrecycledchildren(boolean hasRecycledChildren) {
        this.hasRecycledChildren = hasRecycledChildren;
    }
    public boolean getRecycled() {
        return recycled;
    }

    public void setRecycled(boolean recycled) {
        this.recycled = recycled;
    }


}