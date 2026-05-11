





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Notebook  {

    private boolean hasWLAN;
    private String OperatingSystem;



    public VorkursModel_Notebook(
        boolean hasWLAN,        String OperatingSystem    ) {
        this.hasWLAN = hasWLAN;
        this.OperatingSystem = OperatingSystem;
    }


    public boolean getHaswlan() {
        return hasWLAN;
    }

    public void setHaswlan(boolean hasWLAN) {
        this.hasWLAN = hasWLAN;
    }
    public String getOperatingsystem() {
        return OperatingSystem;
    }

    public void setOperatingsystem(String OperatingSystem) {
        this.OperatingSystem = OperatingSystem;
    }


}