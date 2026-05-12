





import java.util.List;
import java.util.ArrayList;

public class AgendaPartage  {






    private List<EmployeAdministratif> employeadministratifs;


    public AgendaPartage(
    ) {
        this.employeadministratifs = new ArrayList<>();
    }

    public AgendaPartage(
        ArrayList<EmployeAdministratif> employeadministratifs    ) {
        this.employeadministratifs = employeadministratifs;
    }


    public List<EmployeAdministratif> getEmployeadministratifs() {
        return employeadministratifs;
    }

    public void addEmployeadministratif(Employeadministratif employeadministratif) {
        this.employeadministratifs.add(employeadministratif);
    }

}