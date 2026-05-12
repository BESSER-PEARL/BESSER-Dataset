





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_DeuctionTypes  {

    private int id;
    private String date_add;
    private String type;



    public Class_Diagram_for_Propsed_System_DeuctionTypes(
        int id,        String date_add,        String type    ) {
        this.id = id;
        this.date_add = date_add;
        this.type = type;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDate_add() {
        return date_add;
    }

    public void setDate_add(String date_add) {
        this.date_add = date_add;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}