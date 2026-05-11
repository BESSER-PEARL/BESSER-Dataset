





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_RecordField  {

    private String name;





    private OPLmetamodel_AbstractType oplmetamodel_abstracttype;




    private OPLmetamodel_Record oplmetamodel_record;


    public OPLmetamodel_RecordField(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OPLmetamodel_AbstractType getOplmetamodel_abstracttype() {
        return oplmetamodel_abstracttype;
    }

    public void setOplmetamodel_abstracttype(OPLmetamodel_AbstractType oplmetamodel_abstracttype) {
        this.oplmetamodel_abstracttype = oplmetamodel_abstracttype;
    }
    public OPLmetamodel_Record getOplmetamodel_record() {
        return oplmetamodel_record;
    }

    public void setOplmetamodel_record(OPLmetamodel_Record oplmetamodel_record) {
        this.oplmetamodel_record = oplmetamodel_record;
    }

}