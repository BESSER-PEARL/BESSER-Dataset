





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlDataType  {

    private String name;





    private ddlDsl_Column ddldsl_column;


    public ddlDsl_SqlDataType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ddlDsl_Column getDdldsl_column() {
        return ddldsl_column;
    }

    public void setDdldsl_column(ddlDsl_Column ddldsl_column) {
        this.ddldsl_column = ddldsl_column;
    }

}