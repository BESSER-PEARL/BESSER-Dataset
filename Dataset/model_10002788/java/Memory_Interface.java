





import java.util.List;
import java.util.ArrayList;

public class Memory_Interface  {






    private List<car> cars;




    private List<_unnamed> _unnameds;


    public Memory_Interface(
    ) {
        this.cars = new ArrayList<>();
        this._unnameds = new ArrayList<>();
    }

    public Memory_Interface(
        ArrayList<car> cars,        ArrayList<_unnamed> _unnameds    ) {
        this.cars = cars;
        this._unnameds = _unnameds;
    }


    public List<car> getCars() {
        return cars;
    }

    public void addCar(Car car) {
        this.cars.add(car);
    }
    public List<_unnamed> get_unnameds() {
        return _unnameds;
    }

    public void add_unnamed(_unnamed _unnamed) {
        this._unnameds.add(_unnamed);
    }

}