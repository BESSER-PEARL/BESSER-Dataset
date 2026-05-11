





import java.util.List;
import java.util.ArrayList;

public class aadl2_AbstractClassifier extends Abstract, ComponentClassifier {






    private aadl2_Subcomponent aadl2_subcomponent;


    public aadl2_AbstractClassifier(
    ) {
        super(
        );
    }



    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }

}