





import java.util.List;
import java.util.ArrayList;

public class noreflectioncompany_Company  {

    private String name;
    private String size;





    private noreflectioncompany_Employee noreflectioncompany_employee;




    private List<noreflectioncompany_Employee> noreflectioncompany_employees;


    public noreflectioncompany_Company(
        String name,        String size    ) {
        this.name = name;
        this.size = size;
        this.noreflectioncompany_employees = new ArrayList<>();
    }

    public noreflectioncompany_Company(
        String name,        String size        ArrayList<noreflectioncompany_Employee> noreflectioncompany_employees    ) {
        this.name = name;
        this.size = size;
        this.noreflectioncompany_employees = noreflectioncompany_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public noreflectioncompany_Employee getNoreflectioncompany_employee() {
        return noreflectioncompany_employee;
    }

    public void setNoreflectioncompany_employee(noreflectioncompany_Employee noreflectioncompany_employee) {
        this.noreflectioncompany_employee = noreflectioncompany_employee;
    }
    public List<noreflectioncompany_Employee> getNoreflectioncompany_employees() {
        return noreflectioncompany_employees;
    }

    public void addNoreflectioncompany_employee(Noreflectioncompany_employee noreflectioncompany_employee) {
        this.noreflectioncompany_employees.add(noreflectioncompany_employee);
    }

}