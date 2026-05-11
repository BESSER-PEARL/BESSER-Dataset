





import java.util.List;
import java.util.ArrayList;

public class nuSMV_ComputeSpecification extends ModuleElement {

    private String minMax;



    public nuSMV_ComputeSpecification(
        String minMax    ) {
        super(
        );
        this.minMax = minMax;
    }


    public String getMinmax() {
        return minMax;
    }

    public void setMinmax(String minMax) {
        this.minMax = minMax;
    }


}