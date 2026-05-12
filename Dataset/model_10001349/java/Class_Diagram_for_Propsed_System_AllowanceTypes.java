





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_AllowanceTypes  {

    private int type;
    private None date_added;
    private int id;



    public Class_Diagram_for_Propsed_System_AllowanceTypes(
        int type,        None date_added,        int id    ) {
        this.type = type;
        this.date_added = date_added;
        this.id = id;
    }


    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public None getDate_added() {
        return date_added;
    }

    public void setDate_added(None date_added) {
        this.date_added = date_added;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}