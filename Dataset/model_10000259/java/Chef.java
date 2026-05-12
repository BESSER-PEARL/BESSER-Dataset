





import java.util.List;
import java.util.ArrayList;

public class Chef  {

    private int chefid;
    private String name;



    public Chef(
        int chefid,        String name    ) {
        this.chefid = chefid;
        this.name = name;
    }


    public int getChefid() {
        return chefid;
    }

    public void setChefid(int chefid) {
        this.chefid = chefid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}