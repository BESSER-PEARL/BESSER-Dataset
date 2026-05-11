





import java.util.List;
import java.util.ArrayList;

public class adb_RecordComponentAssociationList extends RecordAggregate {

    private boolean nullRecord;





    private adb_ExtensionAggregate adb_extensionaggregate;


    public adb_RecordComponentAssociationList(
        boolean nullRecord    ) {
        super(
        );
        this.nullRecord = nullRecord;
    }


    public boolean getNullrecord() {
        return nullRecord;
    }

    public void setNullrecord(boolean nullRecord) {
        this.nullRecord = nullRecord;
    }

    public adb_ExtensionAggregate getAdb_extensionaggregate() {
        return adb_extensionaggregate;
    }

    public void setAdb_extensionaggregate(adb_ExtensionAggregate adb_extensionaggregate) {
        this.adb_extensionaggregate = adb_extensionaggregate;
    }

}