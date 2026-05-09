





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_CompoundValue extends StructuredValue {






    private List<Kernel_FeatureValue> kernel_featurevalues;


    public fuml_Kernel_CompoundValue(
    ) {
        super(
        );
        this.kernel_featurevalues = new ArrayList<>();
    }

    public fuml_Kernel_CompoundValue(
        ArrayList<Kernel_FeatureValue> kernel_featurevalues    ) {
        this.kernel_featurevalues = kernel_featurevalues;
    }


    public List<Kernel_FeatureValue> getKernel_featurevalues() {
        return kernel_featurevalues;
    }

    public void addKernel_featurevalue(Kernel_featurevalue kernel_featurevalue) {
        this.kernel_featurevalues.add(kernel_featurevalue);
    }

}