





import java.util.List;
import java.util.ArrayList;

public class _unnamed  {






    private List<car> cars;


    public _unnamed(
    ) {
        this.cars = new ArrayList<>();
    }

    public _unnamed(
        ArrayList<car> cars    ) {
        this.cars = cars;
    }


    public List<car> getCars() {
        return cars;
    }

    public void addCar(Car car) {
        this.cars.add(car);
    }

}