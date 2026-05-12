





import java.util.List;
import java.util.ArrayList;

public class Place  {

    private String Details;
    private String Name;



    public Place(
        String Details,        String Name    ) {
        this.Details = Details;
        this.Name = Name;
    }


    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}