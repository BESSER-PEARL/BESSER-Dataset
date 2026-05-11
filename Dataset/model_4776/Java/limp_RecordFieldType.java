





import java.util.List;
import java.util.ArrayList;

public class limp_RecordFieldType  {

    private String fieldName;





    private limp_RecordTypeDef limp_recordtypedef;




    private limp_Type limp_type;


    public limp_RecordFieldType(
        String fieldName    ) {
        this.fieldName = fieldName;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }

    public limp_RecordTypeDef getLimp_recordtypedef() {
        return limp_recordtypedef;
    }

    public void setLimp_recordtypedef(limp_RecordTypeDef limp_recordtypedef) {
        this.limp_recordtypedef = limp_recordtypedef;
    }
    public limp_Type getLimp_type() {
        return limp_type;
    }

    public void setLimp_type(limp_Type limp_type) {
        this.limp_type = limp_type;
    }

}