





import java.util.List;
import java.util.ArrayList;

public class Weekly_Chart  {

    private int Steps;
    private String Name;
    private String CaloriesBurnt;



    public Weekly_Chart(
        int Steps,        String Name,        String CaloriesBurnt    ) {
        this.Steps = Steps;
        this.Name = Name;
        this.CaloriesBurnt = CaloriesBurnt;
    }


    public int getSteps() {
        return Steps;
    }

    public void setSteps(int Steps) {
        this.Steps = Steps;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getCaloriesburnt() {
        return CaloriesBurnt;
    }

    public void setCaloriesburnt(String CaloriesBurnt) {
        this.CaloriesBurnt = CaloriesBurnt;
    }


}