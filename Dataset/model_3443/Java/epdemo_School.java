





import java.util.List;
import java.util.ArrayList;

public class epdemo_School  {

    private String Id;
    private String Name;



    public epdemo_School(
        String Id,        String Name    ) {
        this.Id = Id;
        this.Name = Name;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}