





import java.util.List;
import java.util.ArrayList;

public class library_Shelf  {

    private String name;





    private library_Employee library_employee;


    public library_Shelf(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library_Employee getLibrary_employee() {
        return library_employee;
    }

    public void setLibrary_employee(library_Employee library_employee) {
        this.library_employee = library_employee;
    }

}