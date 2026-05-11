





import java.util.List;
import java.util.ArrayList;

public class adb_RecordDefinition  {

    private String null;





    private adb_ComponentList adb_componentlist;




    private adb_RecordExtensionPart adb_recordextensionpart;




    private adb_RecordTypeDefinition adb_recordtypedefinition;


    public adb_RecordDefinition(
        String null    ) {
        this.null = null;
    }


    public String getNull() {
        return null;
    }

    public void setNull(String null) {
        this.null = null;
    }

    public adb_ComponentList getAdb_componentlist() {
        return adb_componentlist;
    }

    public void setAdb_componentlist(adb_ComponentList adb_componentlist) {
        this.adb_componentlist = adb_componentlist;
    }
    public adb_RecordExtensionPart getAdb_recordextensionpart() {
        return adb_recordextensionpart;
    }

    public void setAdb_recordextensionpart(adb_RecordExtensionPart adb_recordextensionpart) {
        this.adb_recordextensionpart = adb_recordextensionpart;
    }
    public adb_RecordTypeDefinition getAdb_recordtypedefinition() {
        return adb_recordtypedefinition;
    }

    public void setAdb_recordtypedefinition(adb_RecordTypeDefinition adb_recordtypedefinition) {
        this.adb_recordtypedefinition = adb_recordtypedefinition;
    }

}