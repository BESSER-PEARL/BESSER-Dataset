





import java.util.List;
import java.util.ArrayList;

public class ddl_DataType extends DataElement {






    private ddl_Schema ddl_schema;




    private ddl_Column ddl_column;


    public ddl_DataType(
    ) {
        super(
        );
    }



    public ddl_Schema getDdl_schema() {
        return ddl_schema;
    }

    public void setDdl_schema(ddl_Schema ddl_schema) {
        this.ddl_schema = ddl_schema;
    }
    public ddl_Column getDdl_column() {
        return ddl_column;
    }

    public void setDdl_column(ddl_Column ddl_column) {
        this.ddl_column = ddl_column;
    }

}