





import java.util.List;
import java.util.ArrayList;

public class Tescher  {

    private String City;
    private String Name;
    private int t_id;



    public Tescher(
        String City,        String Name,        int t_id    ) {
        this.City = City;
        this.Name = Name;
        this.t_id = t_id;
    }


    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getT_id() {
        return t_id;
    }

    public void setT_id(int t_id) {
        this.t_id = t_id;
    }


}