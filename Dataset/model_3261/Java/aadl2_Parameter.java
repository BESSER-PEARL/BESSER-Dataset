





import java.util.List;
import java.util.ArrayList;

public class aadl2_Parameter extends DirectedFeature, Context, ParameterConnectionEnd {






    private aadl2_DataClassifier aadl2_dataclassifier;




    private aadl2_SubprogramType aadl2_subprogramtype;


    public aadl2_Parameter(
    ) {
        super(
        );
    }



    public aadl2_DataClassifier getAadl2_dataclassifier() {
        return aadl2_dataclassifier;
    }

    public void setAadl2_dataclassifier(aadl2_DataClassifier aadl2_dataclassifier) {
        this.aadl2_dataclassifier = aadl2_dataclassifier;
    }
    public aadl2_SubprogramType getAadl2_subprogramtype() {
        return aadl2_subprogramtype;
    }

    public void setAadl2_subprogramtype(aadl2_SubprogramType aadl2_subprogramtype) {
        this.aadl2_subprogramtype = aadl2_subprogramtype;
    }

}