





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String Id;
    private String Date;
    private String Type;
    private String Description;



    public Booking(
        String Id,        String Date,        String Type,        String Description    ) {
        this.Id = Id;
        this.Date = Date;
        this.Type = Type;
        this.Description = Description;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }


}