





import java.util.List;
import java.util.ArrayList;

public class Count_Steps_and_Calories  {

    private int Steps;
    private String CaloriesBurnt;
    private String Name;



    public Count_Steps_and_Calories(
        int Steps,        String CaloriesBurnt,        String Name    ) {
        this.Steps = Steps;
        this.CaloriesBurnt = CaloriesBurnt;
        this.Name = Name;
    }


    public int getSteps() {
        return Steps;
    }

    public void setSteps(int Steps) {
        this.Steps = Steps;
    }
    public String getCaloriesburnt() {
        return CaloriesBurnt;
    }

    public void setCaloriesburnt(String CaloriesBurnt) {
        this.CaloriesBurnt = CaloriesBurnt;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}