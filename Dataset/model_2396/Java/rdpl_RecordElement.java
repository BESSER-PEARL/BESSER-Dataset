





import java.util.List;
import java.util.ArrayList;

public class rdpl_RecordElement  {

    private String value;





    private rdpl_Record rdpl_record;




    private rdpl_Column rdpl_column;


    public rdpl_RecordElement(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public rdpl_Record getRdpl_record() {
        return rdpl_record;
    }

    public void setRdpl_record(rdpl_Record rdpl_record) {
        this.rdpl_record = rdpl_record;
    }
    public rdpl_Column getRdpl_column() {
        return rdpl_column;
    }

    public void setRdpl_column(rdpl_Column rdpl_column) {
        this.rdpl_column = rdpl_column;
    }

}