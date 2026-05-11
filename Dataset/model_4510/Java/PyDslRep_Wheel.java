





import java.util.List;
import java.util.ArrayList;

public class PyDslRep_Wheel extends Entity {

    private String radius;
    private String name;



    public PyDslRep_Wheel(
        String radius,        String name    ) {
        super(
        );
        this.radius = radius;
        this.name = name;
    }


    public String getRadius() {
        return radius;
    }

    public void setRadius(String radius) {
        this.radius = radius;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}