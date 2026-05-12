





import java.util.List;
import java.util.ArrayList;

public class RDV  {

    private String heure;
    private int duree;
    private String date;





    private List<EmployeAdministratif> employeadministratifs;


    public RDV(
        String heure,        int duree,        String date    ) {
        this.heure = heure;
        this.duree = duree;
        this.date = date;
        this.employeadministratifs = new ArrayList<>();
    }

    public RDV(
        String heure,        int duree,        String date        ArrayList<EmployeAdministratif> employeadministratifs    ) {
        this.heure = heure;
        this.duree = duree;
        this.date = date;
        this.employeadministratifs = employeadministratifs;
    }

    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }
    public int getDuree() {
        return duree;
    }

    public void setDuree(int duree) {
        this.duree = duree;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public List<EmployeAdministratif> getEmployeadministratifs() {
        return employeadministratifs;
    }

    public void addEmployeadministratif(Employeadministratif employeadministratif) {
        this.employeadministratifs.add(employeadministratif);
    }

}