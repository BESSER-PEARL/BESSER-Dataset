





import java.util.List;
import java.util.ArrayList;

public class aadl2_BasicProperty extends TypedElement {

    private String list;





    private aadl2_RecordType aadl2_recordtype;




    private aadl2_BasicPropertyAssociation aadl2_basicpropertyassociation;


    public aadl2_BasicProperty(
        String list    ) {
        super(
        );
        this.list = list;
    }


    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }

    public aadl2_RecordType getAadl2_recordtype() {
        return aadl2_recordtype;
    }

    public void setAadl2_recordtype(aadl2_RecordType aadl2_recordtype) {
        this.aadl2_recordtype = aadl2_recordtype;
    }
    public aadl2_BasicPropertyAssociation getAadl2_basicpropertyassociation() {
        return aadl2_basicpropertyassociation;
    }

    public void setAadl2_basicpropertyassociation(aadl2_BasicPropertyAssociation aadl2_basicpropertyassociation) {
        this.aadl2_basicpropertyassociation = aadl2_basicpropertyassociation;
    }

}