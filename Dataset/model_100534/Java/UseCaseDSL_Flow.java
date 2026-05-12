





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_Flow  {

    private String finalState;



    public UseCaseDSL_Flow(
        String finalState    ) {
        this.finalState = finalState;
    }


    public String getFinalstate() {
        return finalState;
    }

    public void setFinalstate(String finalState) {
        this.finalState = finalState;
    }


}