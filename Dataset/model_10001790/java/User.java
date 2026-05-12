





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Name;
    private String Path_Drawn;
    private String Calories_Burnt;
    private int Weight;
    private int Steps;



    public User(
        String Name,        String Path_Drawn,        String Calories_Burnt,        int Weight,        int Steps    ) {
        this.Name = Name;
        this.Path_Drawn = Path_Drawn;
        this.Calories_Burnt = Calories_Burnt;
        this.Weight = Weight;
        this.Steps = Steps;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPath_drawn() {
        return Path_Drawn;
    }

    public void setPath_drawn(String Path_Drawn) {
        this.Path_Drawn = Path_Drawn;
    }
    public String getCalories_burnt() {
        return Calories_Burnt;
    }

    public void setCalories_burnt(String Calories_Burnt) {
        this.Calories_Burnt = Calories_Burnt;
    }
    public int getWeight() {
        return Weight;
    }

    public void setWeight(int Weight) {
        this.Weight = Weight;
    }
    public int getSteps() {
        return Steps;
    }

    public void setSteps(int Steps) {
        this.Steps = Steps;
    }


}