





import java.util.List;
import java.util.ArrayList;

public class Delivery  {

    private String Date;
    private String Name;
    private String Type;



    public Delivery(
        String Date,        String Name,        String Type    ) {
        this.Date = Date;
        this.Name = Name;
        this.Type = Type;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
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


}