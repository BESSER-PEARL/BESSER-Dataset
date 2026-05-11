





import java.util.List;
import java.util.ArrayList;

public class pascal_record_type  {

    private String endKeyword;
    private String recordKeyword;





    private pascal_unpacked_structured_type pascal_unpacked_structured_type;


    public pascal_record_type(
        String endKeyword,        String recordKeyword    ) {
        this.endKeyword = endKeyword;
        this.recordKeyword = recordKeyword;
    }


    public String getEndkeyword() {
        return endKeyword;
    }

    public void setEndkeyword(String endKeyword) {
        this.endKeyword = endKeyword;
    }
    public String getRecordkeyword() {
        return recordKeyword;
    }

    public void setRecordkeyword(String recordKeyword) {
        this.recordKeyword = recordKeyword;
    }

    public pascal_unpacked_structured_type getPascal_unpacked_structured_type() {
        return pascal_unpacked_structured_type;
    }

    public void setPascal_unpacked_structured_type(pascal_unpacked_structured_type pascal_unpacked_structured_type) {
        this.pascal_unpacked_structured_type = pascal_unpacked_structured_type;
    }

}