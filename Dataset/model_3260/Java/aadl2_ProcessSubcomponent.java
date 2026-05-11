





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessSubcomponent extends Process, Subcomponent {






    private aadl2_SystemImplementation aadl2_systemimplementation;




    private aadl2_ProcessClassifier aadl2_processclassifier;


    public aadl2_ProcessSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_SystemImplementation getAadl2_systemimplementation() {
        return aadl2_systemimplementation;
    }

    public void setAadl2_systemimplementation(aadl2_SystemImplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementation = aadl2_systemimplementation;
    }
    public aadl2_ProcessClassifier getAadl2_processclassifier() {
        return aadl2_processclassifier;
    }

    public void setAadl2_processclassifier(aadl2_ProcessClassifier aadl2_processclassifier) {
        this.aadl2_processclassifier = aadl2_processclassifier;
    }

}