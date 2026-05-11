





import java.util.List;
import java.util.ArrayList;

public class dDL_Constraint  {

    private String id;





    private dDL_Alter_table ddl_alter_table;




    private dDL_Create_table ddl_create_table;


    public dDL_Constraint(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dDL_Alter_table getDdl_alter_table() {
        return ddl_alter_table;
    }

    public void setDdl_alter_table(dDL_Alter_table ddl_alter_table) {
        this.ddl_alter_table = ddl_alter_table;
    }
    public dDL_Create_table getDdl_create_table() {
        return ddl_create_table;
    }

    public void setDdl_create_table(dDL_Create_table ddl_create_table) {
        this.ddl_create_table = ddl_create_table;
    }

}