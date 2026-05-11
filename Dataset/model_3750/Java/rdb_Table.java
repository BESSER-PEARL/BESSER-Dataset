





import java.util.List;
import java.util.ArrayList;

public class rdb_Table  {

    private String schema;
    private String logicalName;
    private String name;
    private String constraints;
    private String comment;



    public rdb_Table(
        String schema,        String logicalName,        String name,        String constraints,        String comment    ) {
        this.schema = schema;
        this.logicalName = logicalName;
        this.name = name;
        this.constraints = constraints;
        this.comment = comment;
    }


    public String getSchema() {
        return schema;
    }

    public void setSchema(String schema) {
        this.schema = schema;
    }
    public String getLogicalname() {
        return logicalName;
    }

    public void setLogicalname(String logicalName) {
        this.logicalName = logicalName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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


}