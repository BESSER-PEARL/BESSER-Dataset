





import java.util.List;
import java.util.ArrayList;

public class Chef  {

    private String name;
    private int chefID;
    private String branch;



    public Chef(
        String name,        int chefID,        String branch    ) {
        this.name = name;
        this.chefID = chefID;
        this.branch = branch;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getChefid() {
        return chefID;
    }

    public void setChefid(int chefID) {
        this.chefID = chefID;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }


}