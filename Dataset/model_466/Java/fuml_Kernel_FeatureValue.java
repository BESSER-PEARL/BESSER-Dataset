





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_FeatureValue  {

    private int position;





    private Kernel_StructuralFeature kernel_structuralfeature;


    public fuml_Kernel_FeatureValue(
        int position    ) {
        this.position = position;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public Kernel_StructuralFeature getKernel_structuralfeature() {
        return kernel_structuralfeature;
    }

    public void setKernel_structuralfeature(Kernel_StructuralFeature kernel_structuralfeature) {
        this.kernel_structuralfeature = kernel_structuralfeature;
    }

}