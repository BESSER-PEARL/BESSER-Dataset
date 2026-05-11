





import java.util.List;
import java.util.ArrayList;

public class aadl2_DataType extends DataClassifier, ComponentType, CallContext {






    private List<aadl2_SubprogramAccess> aadl2_subprogramaccesss;




    private List<aadl2_DataAccess> aadl2_dataaccesss;


    public aadl2_DataType(
    ) {
        super(
        );
        this.aadl2_subprogramaccesss = new ArrayList<>();
        this.aadl2_dataaccesss = new ArrayList<>();
    }

    public aadl2_DataType(
        ArrayList<aadl2_SubprogramAccess> aadl2_subprogramaccesss,        ArrayList<aadl2_DataAccess> aadl2_dataaccesss    ) {
        this.aadl2_subprogramaccesss = aadl2_subprogramaccesss;
        this.aadl2_dataaccesss = aadl2_dataaccesss;
    }


    public List<aadl2_SubprogramAccess> getAadl2_subprogramaccesss() {
        return aadl2_subprogramaccesss;
    }

    public void addAadl2_subprogramaccess(Aadl2_subprogramaccess aadl2_subprogramaccess) {
        this.aadl2_subprogramaccesss.add(aadl2_subprogramaccess);
    }
    public List<aadl2_DataAccess> getAadl2_dataaccesss() {
        return aadl2_dataaccesss;
    }

    public void addAadl2_dataaccess(Aadl2_dataaccess aadl2_dataaccess) {
        this.aadl2_dataaccesss.add(aadl2_dataaccess);
    }

}