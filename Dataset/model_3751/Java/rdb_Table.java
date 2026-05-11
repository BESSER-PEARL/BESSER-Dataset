





import java.util.List;
import java.util.ArrayList;

public class rdb_Table  {

    private String name;
    private String logicalName;
    private String constraints;
    private String comment;





    private rdb_DB rdb_db;




    private rdb_DB rdb_db;


    public rdb_Table(
        String name,        String logicalName,        String constraints,        String comment    ) {
        this.name = name;
        this.logicalName = logicalName;
        this.constraints = constraints;
        this.comment = comment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLogicalname() {
        return logicalName;
    }

    public void setLogicalname(String logicalName) {
        this.logicalName = logicalName;
    }
    public String getConstraints() {
        return constraints;
    }

    public void setConstraints(String constraints) {
        this.constraints = constraints;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }
    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }

}