





import java.util.List;
import java.util.ArrayList;

public class aadl2_DeviceSubcomponent extends Device, Subcomponent {






    private aadl2_DeviceClassifier aadl2_deviceclassifier;




    private aadl2_SystemImplementation aadl2_systemimplementation;


    public aadl2_DeviceSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_DeviceClassifier getAadl2_deviceclassifier() {
        return aadl2_deviceclassifier;
    }

    public void setAadl2_deviceclassifier(aadl2_DeviceClassifier aadl2_deviceclassifier) {
        this.aadl2_deviceclassifier = aadl2_deviceclassifier;
    }
    public aadl2_SystemImplementation getAadl2_systemimplementation() {
        return aadl2_systemimplementation;
    }

    public void setAadl2_systemimplementation(aadl2_SystemImplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementation = aadl2_systemimplementation;
    }

}