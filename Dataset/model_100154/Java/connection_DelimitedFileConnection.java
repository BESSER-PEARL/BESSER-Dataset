





import java.util.List;
import java.util.ArrayList;

public class connection_DelimitedFileConnection extends FileConnection {

    private String FieldSeparatorType;
    private boolean splitRecord;



    public connection_DelimitedFileConnection(
        String FieldSeparatorType,        boolean splitRecord    ) {
        super(
        );
        this.FieldSeparatorType = FieldSeparatorType;
        this.splitRecord = splitRecord;
    }


    public String getFieldseparatortype() {
        return FieldSeparatorType;
    }

    public void setFieldseparatortype(String FieldSeparatorType) {
        this.FieldSeparatorType = FieldSeparatorType;
    }
    public boolean getSplitrecord() {
        return splitRecord;
    }

    public void setSplitrecord(boolean splitRecord) {
        this.splitRecord = splitRecord;
    }


}