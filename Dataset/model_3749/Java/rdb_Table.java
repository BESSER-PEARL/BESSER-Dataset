





import java.util.List;
import java.util.ArrayList;

public class rdb_Table  {

    private String comment;
    private String name;
    private String logicalName;
    private String constraints;





    private List<rdb_Column> rdb_columns;




    private rdb_DB rdb_db;




    private rdb_Column rdb_column;




    private rdb_UserComment rdb_usercomment;




    private rdb_DB rdb_db;


    public rdb_Table(
        String comment,        String name,        String logicalName,        String constraints    ) {
        this.comment = comment;
        this.name = name;
        this.logicalName = logicalName;
        this.constraints = constraints;
        this.rdb_columns = new ArrayList<>();
    }

    public rdb_Table(
        String comment,        String name,        String logicalName,        String constraints        ArrayList<rdb_Column> rdb_columns    ) {
        this.comment = comment;
        this.name = name;
        this.logicalName = logicalName;
        this.constraints = constraints;
        this.rdb_columns = rdb_columns;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
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

    public List<rdb_Column> getRdb_columns() {
        return rdb_columns;
    }

    public void addRdb_column(Rdb_column rdb_column) {
        this.rdb_columns.add(rdb_column);
    }
    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }
    public rdb_Column getRdb_column() {
        return rdb_column;
    }

    public void setRdb_column(rdb_Column rdb_column) {
        this.rdb_column = rdb_column;
    }
    public rdb_UserComment getRdb_usercomment() {
        return rdb_usercomment;
    }

    public void setRdb_usercomment(rdb_UserComment rdb_usercomment) {
        this.rdb_usercomment = rdb_usercomment;
    }
    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }

}