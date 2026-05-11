





import java.util.List;
import java.util.ArrayList;

public class pyrep_Wheel extends Entity {

    private String name;
    private String radius;



    public pyrep_Wheel(
        String name,        String radius    ) {
        super(
        );
        this.name = name;
        this.radius = radius;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRadius() {
        return radius;
    }

    public void setRadius(String radius) {
        this.radius = radius;
    }


}