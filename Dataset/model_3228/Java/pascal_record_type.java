





import java.util.List;
import java.util.ArrayList;

public class pascal_record_type  {

    private String end;
    private String record;





    private pascal_unpacked_structured_type pascal_unpacked_structured_type;


    public pascal_record_type(
        String end,        String record    ) {
        this.end = end;
        this.record = record;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getRecord() {
        return record;
    }

    public void setRecord(String record) {
        this.record = record;
    }

    public pascal_unpacked_structured_type getPascal_unpacked_structured_type() {
        return pascal_unpacked_structured_type;
    }

    public void setPascal_unpacked_structured_type(pascal_unpacked_structured_type pascal_unpacked_structured_type) {
        this.pascal_unpacked_structured_type = pascal_unpacked_structured_type;
    }

}