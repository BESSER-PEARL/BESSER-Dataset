





import java.util.List;
import java.util.ArrayList;

public class model_overrides_Move extends overrides_Reference, overrides_Operation {

    private int newIndex;



    public model_overrides_Move(
        int newIndex    ) {
        super(
        );
        this.newIndex = newIndex;
    }


    public int getNewindex() {
        return newIndex;
    }

    public void setNewindex(int newIndex) {
        this.newIndex = newIndex;
    }


}