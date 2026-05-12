





import java.util.List;
import java.util.ArrayList;

public class Program  {

    private String name;





    private List<car> cars;


    public Program(
        String name    ) {
        this.name = name;
        this.cars = new ArrayList<>();
    }

    public Program(
        String name        ArrayList<car> cars    ) {
        this.name = name;
        this.cars = cars;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<car> getCars() {
        return cars;
    }

    public void addCar(Car car) {
        this.cars.add(car);
    }

}