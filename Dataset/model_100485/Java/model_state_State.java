





import java.util.List;
import java.util.ArrayList;

public class model_state_State extends INamedElement {

    private boolean isInitial;



    public model_state_State(
        boolean isInitial    ) {
        super(
        );
        this.isInitial = isInitial;
    }


    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }


}