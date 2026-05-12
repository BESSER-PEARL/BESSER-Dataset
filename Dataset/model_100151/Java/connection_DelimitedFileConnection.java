





import java.util.List;
import java.util.ArrayList;

public class connection_DelimitedFileConnection extends FileConnection {

    private boolean splitRecord;
    private String FieldSeparatorType;



    public connection_DelimitedFileConnection(
        boolean splitRecord,        String FieldSeparatorType    ) {
        super(
        );
        this.splitRecord = splitRecord;
        this.FieldSeparatorType = FieldSeparatorType;
    }


    public boolean getSplitrecord() {
        return splitRecord;
    }

    public void setSplitrecord(boolean splitRecord) {
        this.splitRecord = splitRecord;
    }
    public String getFieldseparatortype() {
        return FieldSeparatorType;
    }

    public void setFieldseparatortype(String FieldSeparatorType) {
        this.FieldSeparatorType = FieldSeparatorType;
    }


}