





import java.util.List;
import java.util.ArrayList;

public class Shopping  {

    private String Name;
    private int Identity;
    private String Location;



    public Shopping(
        String Name,        int Identity,        String Location    ) {
        this.Name = Name;
        this.Identity = Identity;
        this.Location = Location;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getIdentity() {
        return Identity;
    }

    public void setIdentity(int Identity) {
        this.Identity = Identity;
    }
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }


}