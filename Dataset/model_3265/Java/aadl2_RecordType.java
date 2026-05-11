





import java.util.List;
import java.util.ArrayList;

public class aadl2_RecordType extends NonListType, Namespace {






    private List<aadl2_BasicProperty> aadl2_basicpropertys;


    public aadl2_RecordType(
    ) {
        super(
        );
        this.aadl2_basicpropertys = new ArrayList<>();
    }

    public aadl2_RecordType(
        ArrayList<aadl2_BasicProperty> aadl2_basicpropertys    ) {
        this.aadl2_basicpropertys = aadl2_basicpropertys;
    }


    public List<aadl2_BasicProperty> getAadl2_basicpropertys() {
        return aadl2_basicpropertys;
    }

    public void addAadl2_basicproperty(Aadl2_basicproperty aadl2_basicproperty) {
        this.aadl2_basicpropertys.add(aadl2_basicproperty);
    }

}