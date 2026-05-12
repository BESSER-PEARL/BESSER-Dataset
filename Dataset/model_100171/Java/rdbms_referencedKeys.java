





import java.util.List;
import java.util.ArrayList;

public class rdbms_referencedKeys  {

    private String group;





    private rdbms_column rdbms_column;


    public rdbms_referencedKeys(
        String group    ) {
        this.group = group;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public rdbms_column getRdbms_column() {
        return rdbms_column;
    }

    public void setRdbms_column(rdbms_column rdbms_column) {
        this.rdbms_column = rdbms_column;
    }

}