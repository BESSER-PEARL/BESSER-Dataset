





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_tables_ViewTable extends DerivedTable {

    private String checkType;



    public sqlmodel_tables_ViewTable(
        String checkType    ) {
        super(
        );
        this.checkType = checkType;
    }


    public String getChecktype() {
        return checkType;
    }

    public void setChecktype(String checkType) {
        this.checkType = checkType;
    }


}