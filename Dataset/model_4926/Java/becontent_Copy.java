





import java.util.List;
import java.util.ArrayList;

public class becontent_Copy extends ContentCommand {

    private String fieldName1;
    private String fieldName2;



    public becontent_Copy(
        String fieldName1,        String fieldName2    ) {
        super(
        );
        this.fieldName1 = fieldName1;
        this.fieldName2 = fieldName2;
    }


    public String getFieldname1() {
        return fieldName1;
    }

    public void setFieldname1(String fieldName1) {
        this.fieldName1 = fieldName1;
    }
    public String getFieldname2() {
        return fieldName2;
    }

    public void setFieldname2(String fieldName2) {
        this.fieldName2 = fieldName2;
    }


}