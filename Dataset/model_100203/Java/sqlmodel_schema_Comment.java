





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_schema_Comment  {

    private String description;





    private SQLObject sqlobject;


    public sqlmodel_schema_Comment(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public SQLObject getSqlobject() {
        return sqlobject;
    }

    public void setSqlobject(SQLObject sqlobject) {
        this.sqlobject = sqlobject;
    }

}