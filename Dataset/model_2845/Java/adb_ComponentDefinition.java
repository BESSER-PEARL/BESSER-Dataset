





import java.util.List;
import java.util.ArrayList;

public class adb_ComponentDefinition  {

    private boolean aliased;





    private adb_SubtypeIndication adb_subtypeindication;




    private adb_ArrayTypeDefinition adb_arraytypedefinition;


    public adb_ComponentDefinition(
        boolean aliased    ) {
        this.aliased = aliased;
    }


    public boolean getAliased() {
        return aliased;
    }

    public void setAliased(boolean aliased) {
        this.aliased = aliased;
    }

    public adb_SubtypeIndication getAdb_subtypeindication() {
        return adb_subtypeindication;
    }

    public void setAdb_subtypeindication(adb_SubtypeIndication adb_subtypeindication) {
        this.adb_subtypeindication = adb_subtypeindication;
    }
    public adb_ArrayTypeDefinition getAdb_arraytypedefinition() {
        return adb_arraytypedefinition;
    }

    public void setAdb_arraytypedefinition(adb_ArrayTypeDefinition adb_arraytypedefinition) {
        this.adb_arraytypedefinition = adb_arraytypedefinition;
    }

}