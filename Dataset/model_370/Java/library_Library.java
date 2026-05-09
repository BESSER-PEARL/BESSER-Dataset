





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String name;





    private List<library_Shelf> library_shelfs;




    private List<library_Employee> library_employees;


    public library_Library(
        String name    ) {
        this.name = name;
        this.library_shelfs = new ArrayList<>();
        this.library_employees = new ArrayList<>();
    }

    public library_Library(
        String name        ArrayList<library_Shelf> library_shelfs,        ArrayList<library_Employee> library_employees    ) {
        this.name = name;
        this.library_shelfs = library_shelfs;
        this.library_employees = library_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_Shelf> getLibrary_shelfs() {
        return library_shelfs;
    }

    public void addLibrary_shelf(Library_shelf library_shelf) {
        this.library_shelfs.add(library_shelf);
    }
    public List<library_Employee> getLibrary_employees() {
        return library_employees;
    }

    public void addLibrary_employee(Library_employee library_employee) {
        this.library_employees.add(library_employee);
    }

}