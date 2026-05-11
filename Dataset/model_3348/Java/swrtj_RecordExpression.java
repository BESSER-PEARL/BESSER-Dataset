





import java.util.List;
import java.util.ArrayList;

public class swrtj_RecordExpression  {






    private swrtj_Class swrtj_class;




    private swrtj_NestedRecordExpression swrtj_nestedrecordexpression;




    private List<swrtj_BaseRecord> swrtj_baserecords;




    private swrtj_Record swrtj_record;


    public swrtj_RecordExpression(
    ) {
        this.swrtj_baserecords = new ArrayList<>();
    }

    public swrtj_RecordExpression(
        ArrayList<swrtj_BaseRecord> swrtj_baserecords    ) {
        this.swrtj_baserecords = swrtj_baserecords;
    }


    public swrtj_Class getSwrtj_class() {
        return swrtj_class;
    }

    public void setSwrtj_class(swrtj_Class swrtj_class) {
        this.swrtj_class = swrtj_class;
    }
    public swrtj_NestedRecordExpression getSwrtj_nestedrecordexpression() {
        return swrtj_nestedrecordexpression;
    }

    public void setSwrtj_nestedrecordexpression(swrtj_NestedRecordExpression swrtj_nestedrecordexpression) {
        this.swrtj_nestedrecordexpression = swrtj_nestedrecordexpression;
    }
    public List<swrtj_BaseRecord> getSwrtj_baserecords() {
        return swrtj_baserecords;
    }

    public void addSwrtj_baserecord(Swrtj_baserecord swrtj_baserecord) {
        this.swrtj_baserecords.add(swrtj_baserecord);
    }
    public swrtj_Record getSwrtj_record() {
        return swrtj_record;
    }

    public void setSwrtj_record(swrtj_Record swrtj_record) {
        this.swrtj_record = swrtj_record;
    }

}