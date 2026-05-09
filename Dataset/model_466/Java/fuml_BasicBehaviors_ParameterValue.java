





import java.util.List;
import java.util.ArrayList;

public class fuml_BasicBehaviors_ParameterValue  {






    private List<Kernel_Value> kernel_values;




    private Kernel_Parameter kernel_parameter;


    public fuml_BasicBehaviors_ParameterValue(
    ) {
        this.kernel_values = new ArrayList<>();
    }

    public fuml_BasicBehaviors_ParameterValue(
        ArrayList<Kernel_Value> kernel_values    ) {
        this.kernel_values = kernel_values;
    }


    public List<Kernel_Value> getKernel_values() {
        return kernel_values;
    }

    public void addKernel_value(Kernel_value kernel_value) {
        this.kernel_values.add(kernel_value);
    }
    public Kernel_Parameter getKernel_parameter() {
        return kernel_parameter;
    }

    public void setKernel_parameter(Kernel_Parameter kernel_parameter) {
        this.kernel_parameter = kernel_parameter;
    }

}