





import java.util.List;
import java.util.ArrayList;

public class Shopping  {

    private String Location;
    private int Identity;
    private String Name;



    public Shopping(
        String Location,        int Identity,        String Name    ) {
        this.Location = Location;
        this.Identity = Identity;
        this.Name = Name;
    }


    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public int getIdentity() {
        return Identity;
    }

    public void setIdentity(int Identity) {
        this.Identity = Identity;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}