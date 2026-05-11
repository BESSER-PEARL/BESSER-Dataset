





import java.util.List;
import java.util.ArrayList;

public class aadl2_DataSubcomponent extends Subcomponent, ParameterConnectionEnd, PortConnectionEnd, AccessConnectionEnd, Data {






    private aadl2_DataSubcomponentType aadl2_datasubcomponenttype;


    public aadl2_DataSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_DataSubcomponentType getAadl2_datasubcomponenttype() {
        return aadl2_datasubcomponenttype;
    }

    public void setAadl2_datasubcomponenttype(aadl2_DataSubcomponentType aadl2_datasubcomponenttype) {
        this.aadl2_datasubcomponenttype = aadl2_datasubcomponenttype;
    }

}