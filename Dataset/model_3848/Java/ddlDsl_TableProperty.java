





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_TableProperty  {

    private String name;





    private ddlDsl_CreateTable ddldsl_createtable;


    public ddlDsl_TableProperty(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ddlDsl_CreateTable getDdldsl_createtable() {
        return ddldsl_createtable;
    }

    public void setDdldsl_createtable(ddlDsl_CreateTable ddldsl_createtable) {
        this.ddldsl_createtable = ddldsl_createtable;
    }

}