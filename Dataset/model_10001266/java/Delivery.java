





import java.util.List;
import java.util.ArrayList;

public class Delivery  {

    private String Name;
    private String Type;
    private String Date;



    public Delivery(
        String Name,        String Type,        String Date    ) {
        this.Name = Name;
        this.Type = Type;
        this.Date = Date;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }


}