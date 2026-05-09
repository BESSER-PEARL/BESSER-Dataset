





import java.util.List;
import java.util.ArrayList;

public class project_RGB  {

    private String value;





    private project_CellColor project_cellcolor;


    public project_RGB(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public project_CellColor getProject_cellcolor() {
        return project_cellcolor;
    }

    public void setProject_cellcolor(project_CellColor project_cellcolor) {
        this.project_cellcolor = project_cellcolor;
    }

}