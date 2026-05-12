





import java.util.List;
import java.util.ArrayList;

public class Clothes  {

    private String color;
    private String typeofclothe;



    public Clothes(
        String color,        String typeofclothe    ) {
        this.color = color;
        this.typeofclothe = typeofclothe;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getTypeofclothe() {
        return typeofclothe;
    }

    public void setTypeofclothe(String typeofclothe) {
        this.typeofclothe = typeofclothe;
    }


}