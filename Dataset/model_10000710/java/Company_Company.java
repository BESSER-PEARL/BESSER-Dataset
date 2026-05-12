





import java.util.List;
import java.util.ArrayList;

public class Company_Company  {

    private None pilots;
    private String name;
    private None airportEmployees;
    private None stewards;





    private List<Employee_IEmployee_Interface> employee_iemployee_interfaces;


    public Company_Company(
        None pilots,        String name,        None airportEmployees,        None stewards    ) {
        this.pilots = pilots;
        this.name = name;
        this.airportEmployees = airportEmployees;
        this.stewards = stewards;
        this.employee_iemployee_interfaces = new ArrayList<>();
    }

    public Company_Company(
        None pilots,        String name,        None airportEmployees,        None stewards        ArrayList<Employee_IEmployee_Interface> employee_iemployee_interfaces    ) {
        this.pilots = pilots;
        this.name = name;
        this.airportEmployees = airportEmployees;
        this.stewards = stewards;
        this.employee_iemployee_interfaces = employee_iemployee_interfaces;
    }

    public None getPilots() {
        return pilots;
    }

    public void setPilots(None pilots) {
        this.pilots = pilots;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getAirportemployees() {
        return airportEmployees;
    }

    public void setAirportemployees(None airportEmployees) {
        this.airportEmployees = airportEmployees;
    }
    public None getStewards() {
        return stewards;
    }

    public void setStewards(None stewards) {
        this.stewards = stewards;
    }

    public List<Employee_IEmployee_Interface> getEmployee_iemployee_interfaces() {
        return employee_iemployee_interfaces;
    }

    public void addEmployee_iemployee_interface(Employee_iemployee_interface employee_iemployee_interface) {
        this.employee_iemployee_interfaces.add(employee_iemployee_interface);
    }

}