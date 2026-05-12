





import java.util.List;
import java.util.ArrayList;

public class CarRental_CarGroup  {

    private String kind;





    private List<CarRental_Rental> carrental_rentals;




    private List<CarRental_Car> carrental_cars;




    private CarRental_Car carrental_car;




    private CarRental_Rental carrental_rental;




    private CarRental_Branch carrental_branch;




    private CarRental_CarGroup carrental_cargroup;




    private List<CarRental_Branch> carrental_branchs;




    private CarRental_CarGroup carrental_cargroup;


    public CarRental_CarGroup(
        String kind    ) {
        this.kind = kind;
        this.carrental_rentals = new ArrayList<>();
        this.carrental_cars = new ArrayList<>();
        this.carrental_branchs = new ArrayList<>();
    }

    public CarRental_CarGroup(
        String kind        ArrayList<CarRental_Rental> carrental_rentals,        ArrayList<CarRental_Car> carrental_cars,        ArrayList<CarRental_Branch> carrental_branchs    ) {
        this.kind = kind;
        this.carrental_rentals = carrental_rentals;
        this.carrental_cars = carrental_cars;
        this.carrental_branchs = carrental_branchs;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<CarRental_Rental> getCarrental_rentals() {
        return carrental_rentals;
    }

    public void addCarrental_rental(Carrental_rental carrental_rental) {
        this.carrental_rentals.add(carrental_rental);
    }
    public List<CarRental_Car> getCarrental_cars() {
        return carrental_cars;
    }

    public void addCarrental_car(Carrental_car carrental_car) {
        this.carrental_cars.add(carrental_car);
    }
    public CarRental_Car getCarrental_car() {
        return carrental_car;
    }

    public void setCarrental_car(CarRental_Car carrental_car) {
        this.carrental_car = carrental_car;
    }
    public CarRental_Rental getCarrental_rental() {
        return carrental_rental;
    }

    public void setCarrental_rental(CarRental_Rental carrental_rental) {
        this.carrental_rental = carrental_rental;
    }
    public CarRental_Branch getCarrental_branch() {
        return carrental_branch;
    }

    public void setCarrental_branch(CarRental_Branch carrental_branch) {
        this.carrental_branch = carrental_branch;
    }
    public CarRental_CarGroup getCarrental_cargroup() {
        return carrental_cargroup;
    }

    public void setCarrental_cargroup(CarRental_CarGroup carrental_cargroup) {
        this.carrental_cargroup = carrental_cargroup;
    }
    public List<CarRental_Branch> getCarrental_branchs() {
        return carrental_branchs;
    }

    public void addCarrental_branch(Carrental_branch carrental_branch) {
        this.carrental_branchs.add(carrental_branch);
    }
    public CarRental_CarGroup getCarrental_cargroup() {
        return carrental_cargroup;
    }

    public void setCarrental_cargroup(CarRental_CarGroup carrental_cargroup) {
        this.carrental_cargroup = carrental_cargroup;
    }

}