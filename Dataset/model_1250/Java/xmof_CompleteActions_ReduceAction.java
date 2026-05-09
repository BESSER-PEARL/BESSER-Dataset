





import java.util.List;
import java.util.ArrayList;

public class xmof_CompleteActions_ReduceAction extends Action {

    private boolean ordered;



    public xmof_CompleteActions_ReduceAction(
        boolean ordered    ) {
        super(
        );
        this.ordered = ordered;
    }


    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }


}