





import java.util.List;
import java.util.ArrayList;

public class project_Criterion  {

    private String direction;
    private String columnId;





    private project_Sort project_sort;


    public project_Criterion(
        String direction,        String columnId    ) {
        this.direction = direction;
        this.columnId = columnId;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getColumnid() {
        return columnId;
    }

    public void setColumnid(String columnId) {
        this.columnId = columnId;
    }

    public project_Sort getProject_sort() {
        return project_sort;
    }

    public void setProject_sort(project_Sort project_sort) {
        this.project_sort = project_sort;
    }

}