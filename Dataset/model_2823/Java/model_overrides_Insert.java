





import java.util.List;
import java.util.ArrayList;

public class model_overrides_Insert extends Operation {

    private int newIndex;



    public model_overrides_Insert(
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