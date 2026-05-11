





import java.util.List;
import java.util.ArrayList;

public class CarRental2_CarGroup  {

    private String kind;





    private CarRental2_CarGroup carrental2_cargroup;




    private CarRental2_Rental carrental2_rental;




    private List<CarRental2_Rental> carrental2_rentals;




    private CarRental2_CarGroup carrental2_cargroup;




    private CarRental2_Branch carrental2_branch;




    private List<CarRental2_Branch> carrental2_branchs;




    private CarRental2_Car carrental2_car;




    private List<CarRental2_Car> carrental2_cars;


    public CarRental2_CarGroup(
        String kind    ) {
        this.kind = kind;
        this.carrental2_rentals = new ArrayList<>();
        this.carrental2_branchs = new ArrayList<>();
        this.carrental2_cars = new ArrayList<>();
    }

    public CarRental2_CarGroup(
        String kind        ArrayList<CarRental2_Rental> carrental2_rentals,        ArrayList<CarRental2_Branch> carrental2_branchs,        ArrayList<CarRental2_Car> carrental2_cars    ) {
        this.kind = kind;
        this.carrental2_rentals = carrental2_rentals;
        this.carrental2_branchs = carrental2_branchs;
        this.carrental2_cars = carrental2_cars;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public CarRental2_CarGroup getCarrental2_cargroup() {
        return carrental2_cargroup;
    }

    public void setCarrental2_cargroup(CarRental2_CarGroup carrental2_cargroup) {
        this.carrental2_cargroup = carrental2_cargroup;
    }
    public CarRental2_Rental getCarrental2_rental() {
        return carrental2_rental;
    }

    public void setCarrental2_rental(CarRental2_Rental carrental2_rental) {
        this.carrental2_rental = carrental2_rental;
    }
    public List<CarRental2_Rental> getCarrental2_rentals() {
        return carrental2_rentals;
    }

    public void addCarrental2_rental(Carrental2_rental carrental2_rental) {
        this.carrental2_rentals.add(carrental2_rental);
    }
    public CarRental2_CarGroup getCarrental2_cargroup() {
        return carrental2_cargroup;
    }

    public void setCarrental2_cargroup(CarRental2_CarGroup carrental2_cargroup) {
        this.carrental2_cargroup = carrental2_cargroup;
    }
    public CarRental2_Branch getCarrental2_branch() {
        return carrental2_branch;
    }

    public void setCarrental2_branch(CarRental2_Branch carrental2_branch) {
        this.carrental2_branch = carrental2_branch;
    }
    public List<CarRental2_Branch> getCarrental2_branchs() {
        return carrental2_branchs;
    }

    public void addCarrental2_branch(Carrental2_branch carrental2_branch) {
        this.carrental2_branchs.add(carrental2_branch);
    }
    public CarRental2_Car getCarrental2_car() {
        return carrental2_car;
    }

    public void setCarrental2_car(CarRental2_Car carrental2_car) {
        this.carrental2_car = carrental2_car;
    }
    public List<CarRental2_Car> getCarrental2_cars() {
        return carrental2_cars;
    }

    public void addCarrental2_car(Carrental2_car carrental2_car) {
        this.carrental2_cars.add(carrental2_car);
    }

}