





import java.util.List;
import java.util.ArrayList;

public class aadl2_DataSubcomponentType extends SubcomponentType, AbstractFeatureClassifier {






    private aadl2_Parameter aadl2_parameter;




    private aadl2_DataPort aadl2_dataport;




    private aadl2_DataAccess aadl2_dataaccess;




    private aadl2_EventDataPort aadl2_eventdataport;


    public aadl2_DataSubcomponentType(
    ) {
        super(
        );
    }



    public aadl2_Parameter getAadl2_parameter() {
        return aadl2_parameter;
    }

    public void setAadl2_parameter(aadl2_Parameter aadl2_parameter) {
        this.aadl2_parameter = aadl2_parameter;
    }
    public aadl2_DataPort getAadl2_dataport() {
        return aadl2_dataport;
    }

    public void setAadl2_dataport(aadl2_DataPort aadl2_dataport) {
        this.aadl2_dataport = aadl2_dataport;
    }
    public aadl2_DataAccess getAadl2_dataaccess() {
        return aadl2_dataaccess;
    }

    public void setAadl2_dataaccess(aadl2_DataAccess aadl2_dataaccess) {
        this.aadl2_dataaccess = aadl2_dataaccess;
    }
    public aadl2_EventDataPort getAadl2_eventdataport() {
        return aadl2_eventdataport;
    }

    public void setAadl2_eventdataport(aadl2_EventDataPort aadl2_eventdataport) {
        this.aadl2_eventdataport = aadl2_eventdataport;
    }

}