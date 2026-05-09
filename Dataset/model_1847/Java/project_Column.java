





import java.util.List;
import java.util.ArrayList;

public class project_Column  {

    private String id;





    private project_Columns project_columns;


    public project_Column(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public project_Columns getProject_columns() {
        return project_columns;
    }

    public void setProject_columns(project_Columns project_columns) {
        this.project_columns = project_columns;
    }

}