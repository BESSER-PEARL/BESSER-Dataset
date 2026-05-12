





import java.util.List;
import java.util.ArrayList;

public class Update_Data  {

    private int Weight;
    private String Name;



    public Update_Data(
        int Weight,        String Name    ) {
        this.Weight = Weight;
        this.Name = Name;
    }


    public int getWeight() {
        return Weight;
    }

    public void setWeight(int Weight) {
        this.Weight = Weight;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}