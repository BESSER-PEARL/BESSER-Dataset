





import java.util.List;
import java.util.ArrayList;

public class simulink_Chart extends Block, CompositeStateflowElement {

    private String decomposition;



    public simulink_Chart(
        String decomposition    ) {
        super(
        );
        this.decomposition = decomposition;
    }


    public String getDecomposition() {
        return decomposition;
    }

    public void setDecomposition(String decomposition) {
        this.decomposition = decomposition;
    }


}