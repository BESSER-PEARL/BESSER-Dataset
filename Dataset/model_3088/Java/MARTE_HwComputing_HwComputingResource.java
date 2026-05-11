





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwComputing_HwComputingResource extends HwGeneral_HwResource, GRM_ComputingResource {

    private String op_Frequencies;



    public MARTE_HwComputing_HwComputingResource(
        String op_Frequencies    ) {
        super(
        );
        this.op_Frequencies = op_Frequencies;
    }


    public String getOp_frequencies() {
        return op_Frequencies;
    }

    public void setOp_frequencies(String op_Frequencies) {
        this.op_Frequencies = op_Frequencies;
    }


}