





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Notebook  {

    private String OperatingSystem;
    private boolean hasWLAN;





    private VorkursModel_Person vorkursmodel_person;


    public VorkursModel_Notebook(
        String OperatingSystem,        boolean hasWLAN    ) {
        this.OperatingSystem = OperatingSystem;
        this.hasWLAN = hasWLAN;
    }


    public String getOperatingsystem() {
        return OperatingSystem;
    }

    public void setOperatingsystem(String OperatingSystem) {
        this.OperatingSystem = OperatingSystem;
    }
    public boolean getHaswlan() {
        return hasWLAN;
    }

    public void setHaswlan(boolean hasWLAN) {
        this.hasWLAN = hasWLAN;
    }

    public VorkursModel_Person getVorkursmodel_person() {
        return vorkursmodel_person;
    }

    public void setVorkursmodel_person(VorkursModel_Person vorkursmodel_person) {
        this.vorkursmodel_person = vorkursmodel_person;
    }

}