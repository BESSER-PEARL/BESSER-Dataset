





import java.util.List;
import java.util.ArrayList;

public class dDL_ISNULL  {

    private boolean nonNull;
    private boolean null;





    private dDL_Column ddl_column;


    public dDL_ISNULL(
        boolean nonNull,        boolean null    ) {
        this.nonNull = nonNull;
        this.null = null;
    }


    public boolean getNonnull() {
        return nonNull;
    }

    public void setNonnull(boolean nonNull) {
        this.nonNull = nonNull;
    }
    public boolean getNull() {
        return null;
    }

    public void setNull(boolean null) {
        this.null = null;
    }

    public dDL_Column getDdl_column() {
        return ddl_column;
    }

    public void setDdl_column(dDL_Column ddl_column) {
        this.ddl_column = ddl_column;
    }

}