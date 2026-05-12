





import java.util.List;
import java.util.ArrayList;

public class datasetload_DataSourceJdbc extends DataSource {

    private String DefaultSchema;
    private String DataBaseUserPwd;
    private String DataBaseUser;



    public datasetload_DataSourceJdbc(
        String DefaultSchema,        String DataBaseUserPwd,        String DataBaseUser    ) {
        super(
        );
        this.DefaultSchema = DefaultSchema;
        this.DataBaseUserPwd = DataBaseUserPwd;
        this.DataBaseUser = DataBaseUser;
    }


    public String getDefaultschema() {
        return DefaultSchema;
    }

    public void setDefaultschema(String DefaultSchema) {
        this.DefaultSchema = DefaultSchema;
    }
    public String getDatabaseuserpwd() {
        return DataBaseUserPwd;
    }

    public void setDatabaseuserpwd(String DataBaseUserPwd) {
        this.DataBaseUserPwd = DataBaseUserPwd;
    }
    public String getDatabaseuser() {
        return DataBaseUser;
    }

    public void setDatabaseuser(String DataBaseUser) {
        this.DataBaseUser = DataBaseUser;
    }


}