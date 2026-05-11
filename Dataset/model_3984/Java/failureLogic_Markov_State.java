





import java.util.List;
import java.util.ArrayList;

public class failureLogic_Markov_State extends BaseElement {

    private boolean isInitialState;
    private boolean isFailState;



    public failureLogic_Markov_State(
        boolean isInitialState,        boolean isFailState    ) {
        super(
        );
        this.isInitialState = isInitialState;
        this.isFailState = isFailState;
    }


    public boolean getIsinitialstate() {
        return isInitialState;
    }

    public void setIsinitialstate(boolean isInitialState) {
        this.isInitialState = isInitialState;
    }
    public boolean getIsfailstate() {
        return isFailState;
    }

    public void setIsfailstate(boolean isFailState) {
        this.isFailState = isFailState;
    }


}