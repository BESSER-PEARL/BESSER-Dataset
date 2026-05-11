





import java.util.List;
import java.util.ArrayList;

public class genericsGoCrazy_Car  {

    private String fullName;
    private String name;
    private String doors;
    private String color;





    private genericsGoCrazy_Car genericsgocrazy_car;


    public genericsGoCrazy_Car(
        String fullName,        String name,        String doors,        String color    ) {
        this.fullName = fullName;
        this.name = name;
        this.doors = doors;
        this.color = color;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDoors() {
        return doors;
    }

    public void setDoors(String doors) {
        this.doors = doors;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public genericsGoCrazy_Car getGenericsgocrazy_car() {
        return genericsgocrazy_car;
    }

    public void setGenericsgocrazy_car(genericsGoCrazy_Car genericsgocrazy_car) {
        this.genericsgocrazy_car = genericsgocrazy_car;
    }

}