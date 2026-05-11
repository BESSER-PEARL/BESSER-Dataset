





import java.util.List;
import java.util.ArrayList;

public class mid_operator_OperatorInput  {






    private List<ConversionOperator> conversionoperators;




    private operator_mid_ModelEndpoint operator_mid_modelendpoint;


    public mid_operator_OperatorInput(
    ) {
        this.conversionoperators = new ArrayList<>();
    }

    public mid_operator_OperatorInput(
        ArrayList<ConversionOperator> conversionoperators    ) {
        this.conversionoperators = conversionoperators;
    }


    public List<ConversionOperator> getConversionoperators() {
        return conversionoperators;
    }

    public void addConversionoperator(Conversionoperator conversionoperator) {
        this.conversionoperators.add(conversionoperator);
    }
    public operator_mid_ModelEndpoint getOperator_mid_modelendpoint() {
        return operator_mid_modelendpoint;
    }

    public void setOperator_mid_modelendpoint(operator_mid_ModelEndpoint operator_mid_modelendpoint) {
        this.operator_mid_modelendpoint = operator_mid_modelendpoint;
    }

}