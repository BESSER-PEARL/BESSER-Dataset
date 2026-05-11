





import java.util.List;
import java.util.ArrayList;

public class dDL_Colname  {

    private String id;





    private dDL_Comment ddl_comment;


    public dDL_Colname(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dDL_Comment getDdl_comment() {
        return ddl_comment;
    }

    public void setDdl_comment(dDL_Comment ddl_comment) {
        this.ddl_comment = ddl_comment;
    }

}