





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Branch  {

    private String location;





    private CarRental2_Rental carrental2_rental;




    private List<CarRental2_Rental> carrental2_rentals;




    private List<CarRental2_Employee> carrental2_employees;




    private CarRental2_Employee carrental2_employee;




    private CarRental2_Employee carrental2_employee;




    private CarRental2_Employee carrental2_employee;


    public CarRental2_Branch(
        String location    ) {
        this.location = location;
        this.carrental2_rentals = new ArrayList<>();
        this.carrental2_employees = new ArrayList<>();
    }

    public CarRental2_Branch(
        String location        ArrayList<CarRental2_Rental> carrental2_rentals,        ArrayList<CarRental2_Employee> carrental2_employees    ) {
        this.location = location;
        this.carrental2_rentals = carrental2_rentals;
        this.carrental2_employees = carrental2_employees;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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
    public List<CarRental2_Employee> getCarrental2_employees() {
        return carrental2_employees;
    }

    public void addCarrental2_employee(Carrental2_employee carrental2_employee) {
        this.carrental2_employees.add(carrental2_employee);
    }
    public CarRental2_Employee getCarrental2_employee() {
        return carrental2_employee;
    }

    public void setCarrental2_employee(CarRental2_Employee carrental2_employee) {
        this.carrental2_employee = carrental2_employee;
    }
    public CarRental2_Employee getCarrental2_employee() {
        return carrental2_employee;
    }

    public void setCarrental2_employee(CarRental2_Employee carrental2_employee) {
        this.carrental2_employee = carrental2_employee;
    }
    public CarRental2_Employee getCarrental2_employee() {
        return carrental2_employee;
    }

    public void setCarrental2_employee(CarRental2_Employee carrental2_employee) {
        this.carrental2_employee = carrental2_employee;
    }

}