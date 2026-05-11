





import java.util.List;
import java.util.ArrayList;

public class aadl2_DeviceSubcomponent extends Device, Subcomponent {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_DeviceSubcomponentType aadl2_devicesubcomponenttype;


    public aadl2_DeviceSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }
    public aadl2_DeviceSubcomponentType getAadl2_devicesubcomponenttype() {
        return aadl2_devicesubcomponenttype;
    }

    public void setAadl2_devicesubcomponenttype(aadl2_DeviceSubcomponentType aadl2_devicesubcomponenttype) {
        this.aadl2_devicesubcomponenttype = aadl2_devicesubcomponenttype;
    }

}