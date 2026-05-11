





import java.util.List;
import java.util.ArrayList;

public class coCoMM_AggregationFunction  {

    private String operation;





    private coCoMM_OptimizationCC cocomm_optimizationcc;




    private coCoMM_AttributeType cocomm_attributetype;




    private coCoMM_HardLimitCC cocomm_hardlimitcc;


    public coCoMM_AggregationFunction(
        String operation    ) {
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public coCoMM_OptimizationCC getCocomm_optimizationcc() {
        return cocomm_optimizationcc;
    }

    public void setCocomm_optimizationcc(coCoMM_OptimizationCC cocomm_optimizationcc) {
        this.cocomm_optimizationcc = cocomm_optimizationcc;
    }
    public coCoMM_AttributeType getCocomm_attributetype() {
        return cocomm_attributetype;
    }

    public void setCocomm_attributetype(coCoMM_AttributeType cocomm_attributetype) {
        this.cocomm_attributetype = cocomm_attributetype;
    }
    public coCoMM_HardLimitCC getCocomm_hardlimitcc() {
        return cocomm_hardlimitcc;
    }

    public void setCocomm_hardlimitcc(coCoMM_HardLimitCC cocomm_hardlimitcc) {
        this.cocomm_hardlimitcc = cocomm_hardlimitcc;
    }

}