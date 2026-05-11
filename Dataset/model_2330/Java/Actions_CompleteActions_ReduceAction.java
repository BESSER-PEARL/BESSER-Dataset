





import java.util.List;
import java.util.ArrayList;

public class Actions_CompleteActions_ReduceAction extends Action {

    private boolean isOrdered;



    public Actions_CompleteActions_ReduceAction(
        boolean isOrdered    ) {
        super(
        );
        this.isOrdered = isOrdered;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }


}