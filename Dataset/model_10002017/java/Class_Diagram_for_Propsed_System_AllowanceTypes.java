





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_AllowanceTypes  {

    private String date_added;
    private int id;
    private int type;



    public Class_Diagram_for_Propsed_System_AllowanceTypes(
        String date_added,        int id,        int type    ) {
        this.date_added = date_added;
        this.id = id;
        this.type = type;
    }


    public String getDate_added() {
        return date_added;
    }

    public void setDate_added(String date_added) {
        this.date_added = date_added;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }


}