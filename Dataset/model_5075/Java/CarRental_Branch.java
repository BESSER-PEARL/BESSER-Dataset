





import java.util.List;
import java.util.ArrayList;

public class CarRental_Branch  {

    private String location;





    private CarRental_Employee carrental_employee;




    private List<CarRental_Rental> carrental_rentals;




    private CarRental_Employee carrental_employee;




    private CarRental_Rental carrental_rental;




    private CarRental_Employee carrental_employee;




    private List<CarRental_Employee> carrental_employees;


    public CarRental_Branch(
        String location    ) {
        this.location = location;
        this.carrental_rentals = new ArrayList<>();
        this.carrental_employees = new ArrayList<>();
    }

    public CarRental_Branch(
        String location        ArrayList<CarRental_Rental> carrental_rentals,        ArrayList<CarRental_Employee> carrental_employees    ) {
        this.location = location;
        this.carrental_rentals = carrental_rentals;
        this.carrental_employees = carrental_employees;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public CarRental_Employee getCarrental_employee() {
        return carrental_employee;
    }

    public void setCarrental_employee(CarRental_Employee carrental_employee) {
        this.carrental_employee = carrental_employee;
    }
    public List<CarRental_Rental> getCarrental_rentals() {
        return carrental_rentals;
    }

    public void addCarrental_rental(Carrental_rental carrental_rental) {
        this.carrental_rentals.add(carrental_rental);
    }
    public CarRental_Employee getCarrental_employee() {
        return carrental_employee;
    }

    public void setCarrental_employee(CarRental_Employee carrental_employee) {
        this.carrental_employee = carrental_employee;
    }
    public CarRental_Rental getCarrental_rental() {
        return carrental_rental;
    }

    public void setCarrental_rental(CarRental_Rental carrental_rental) {
        this.carrental_rental = carrental_rental;
    }
    public CarRental_Employee getCarrental_employee() {
        return carrental_employee;
    }

    public void setCarrental_employee(CarRental_Employee carrental_employee) {
        this.carrental_employee = carrental_employee;
    }
    public List<CarRental_Employee> getCarrental_employees() {
        return carrental_employees;
    }

    public void addCarrental_employee(Carrental_employee carrental_employee) {
        this.carrental_employees.add(carrental_employee);
    }

}