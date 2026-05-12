





import java.util.List;
import java.util.ArrayList;

public class Ingredient_Box  {

    private float WeightValue;
    private int BoxID;





    private Cooking_System cooking_system;


    public Ingredient_Box(
        float WeightValue,        int BoxID    ) {
        this.WeightValue = WeightValue;
        this.BoxID = BoxID;
    }


    public float getWeightvalue() {
        return WeightValue;
    }

    public void setWeightvalue(float WeightValue) {
        this.WeightValue = WeightValue;
    }
    public int getBoxid() {
        return BoxID;
    }

    public void setBoxid(int BoxID) {
        this.BoxID = BoxID;
    }

    public Cooking_System getCooking_system() {
        return cooking_system;
    }

    public void setCooking_system(Cooking_System cooking_system) {
        this.cooking_system = cooking_system;
    }

}