





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private String Name;
    private String locality;
    private String Name_string;
    private int ID;



    public Bank(
        String Name,        String locality,        String Name_string,        int ID    ) {
        this.Name = Name;
        this.locality = locality;
        this.Name_string = Name_string;
        this.ID = ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getLocality() {
        return locality;
    }

    public void setLocality(String locality) {
        this.locality = locality;
    }
    public String getName_string() {
        return Name_string;
    }

    public void setName_string(String Name_string) {
        this.Name_string = Name_string;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}