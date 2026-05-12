





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String Id;
    private String Type;
    private String Date;
    private String Description;



    public Booking(
        String Id,        String Type,        String Date,        String Description    ) {
        this.Id = Id;
        this.Type = Type;
        this.Date = Date;
        this.Description = Description;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
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
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }


}