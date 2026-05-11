





import java.util.List;
import java.util.ArrayList;

public class dDL_Tabname  {

    private String basename;
    private String id;





    private dDL_Foreign_key ddl_foreign_key;




    private dDL_Comment ddl_comment;




    private dDL_Alter_table ddl_alter_table;


    public dDL_Tabname(
        String basename,        String id    ) {
        this.basename = basename;
        this.id = id;
    }


    public String getBasename() {
        return basename;
    }

    public void setBasename(String basename) {
        this.basename = basename;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dDL_Foreign_key getDdl_foreign_key() {
        return ddl_foreign_key;
    }

    public void setDdl_foreign_key(dDL_Foreign_key ddl_foreign_key) {
        this.ddl_foreign_key = ddl_foreign_key;
    }
    public dDL_Comment getDdl_comment() {
        return ddl_comment;
    }

    public void setDdl_comment(dDL_Comment ddl_comment) {
        this.ddl_comment = ddl_comment;
    }
    public dDL_Alter_table getDdl_alter_table() {
        return ddl_alter_table;
    }

    public void setDdl_alter_table(dDL_Alter_table ddl_alter_table) {
        this.ddl_alter_table = ddl_alter_table;
    }

}