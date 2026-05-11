





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_Alter extends DdlStatement {






    private ddlDsl_CreateTable ddldsl_createtable;


    public ddlDsl_Alter(
    ) {
        super(
        );
    }



    public ddlDsl_CreateTable getDdldsl_createtable() {
        return ddldsl_createtable;
    }

    public void setDdldsl_createtable(ddlDsl_CreateTable ddldsl_createtable) {
        this.ddldsl_createtable = ddldsl_createtable;
    }

}