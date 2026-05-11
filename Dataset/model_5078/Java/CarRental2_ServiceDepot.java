





import java.util.List;
import java.util.ArrayList;

public class CarRental2_ServiceDepot  {

    private String location;





    private List<CarRental2_Car> carrental2_cars;




    private CarRental2_Car carrental2_car;


    public CarRental2_ServiceDepot(
        String location    ) {
        this.location = location;
        this.carrental2_cars = new ArrayList<>();
    }

    public CarRental2_ServiceDepot(
        String location        ArrayList<CarRental2_Car> carrental2_cars    ) {
        this.location = location;
        this.carrental2_cars = carrental2_cars;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<CarRental2_Car> getCarrental2_cars() {
        return carrental2_cars;
    }

    public void addCarrental2_car(Carrental2_car carrental2_car) {
        this.carrental2_cars.add(carrental2_car);
    }
    public CarRental2_Car getCarrental2_car() {
        return carrental2_car;
    }

    public void setCarrental2_car(CarRental2_Car carrental2_car) {
        this.carrental2_car = carrental2_car;
    }

}