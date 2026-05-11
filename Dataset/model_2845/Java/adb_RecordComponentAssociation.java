





import java.util.List;
import java.util.ArrayList;

public class adb_RecordComponentAssociation  {






    private List<adb_ComponentChoiceList> adb_componentchoicelists;




    private adb_RecordComponentAssociationList adb_recordcomponentassociationlist;


    public adb_RecordComponentAssociation(
    ) {
        this.adb_componentchoicelists = new ArrayList<>();
    }

    public adb_RecordComponentAssociation(
        ArrayList<adb_ComponentChoiceList> adb_componentchoicelists    ) {
        this.adb_componentchoicelists = adb_componentchoicelists;
    }


    public List<adb_ComponentChoiceList> getAdb_componentchoicelists() {
        return adb_componentchoicelists;
    }

    public void addAdb_componentchoicelist(Adb_componentchoicelist adb_componentchoicelist) {
        this.adb_componentchoicelists.add(adb_componentchoicelist);
    }
    public adb_RecordComponentAssociationList getAdb_recordcomponentassociationlist() {
        return adb_recordcomponentassociationlist;
    }

    public void setAdb_recordcomponentassociationlist(adb_RecordComponentAssociationList adb_recordcomponentassociationlist) {
        this.adb_recordcomponentassociationlist = adb_recordcomponentassociationlist;
    }

}