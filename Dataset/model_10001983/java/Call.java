





import java.util.List;
import java.util.ArrayList;

public class Call  {

    private String direction;
    private String created;
    private None location;





    private Car car;


    public Call(
        String direction,        String created,        None location    ) {
        this.direction = direction;
        this.created = created;
        this.location = location;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public None getLocation() {
        return location;
    }

    public void setLocation(None location) {
        this.location = location;
    }

    public Car getCar() {
        return car;
    }

    public void setCar(Car car) {
        this.car = car;
    }

}