





import java.util.List;
import java.util.ArrayList;

public class Decoration  {

    private None Decor_type;
    private String Square_feet;
    private String cost;



    public Decoration(
        None Decor_type,        String Square_feet,        String cost    ) {
        this.Decor_type = Decor_type;
        this.Square_feet = Square_feet;
        this.cost = cost;
    }


    public None getDecor_type() {
        return Decor_type;
    }

    public void setDecor_type(None Decor_type) {
        this.Decor_type = Decor_type;
    }
    public String getSquare_feet() {
        return Square_feet;
    }

    public void setSquare_feet(String Square_feet) {
        this.Square_feet = Square_feet;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }


}