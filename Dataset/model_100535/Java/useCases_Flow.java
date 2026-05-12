





import java.util.List;
import java.util.ArrayList;

public class useCases_Flow  {

    private String finalState;



    public useCases_Flow(
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