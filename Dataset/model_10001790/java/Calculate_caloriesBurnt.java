





import java.util.List;
import java.util.ArrayList;

public class Calculate_caloriesBurnt  {

    private String CaloriesBurnt;
    private int Steps;
    private String Name;





    private Count_Steps_and_Calories count_steps_and_calories;


    public Calculate_caloriesBurnt(
        String CaloriesBurnt,        int Steps,        String Name    ) {
        this.CaloriesBurnt = CaloriesBurnt;
        this.Steps = Steps;
        this.Name = Name;
    }


    public String getCaloriesburnt() {
        return CaloriesBurnt;
    }

    public void setCaloriesburnt(String CaloriesBurnt) {
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

    public Count_Steps_and_Calories getCount_steps_and_calories() {
        return count_steps_and_calories;
    }

    public void setCount_steps_and_calories(Count_Steps_and_Calories count_steps_and_calories) {
        this.count_steps_and_calories = count_steps_and_calories;
    }

}