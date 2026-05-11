





import java.util.List;
import java.util.ArrayList;

public class UML2_Class  {

    private boolean isActive;





    private List<UML2_Reception> uml2_receptions;


    public UML2_Class(
        boolean isActive    ) {
        this.isActive = isActive;
        this.uml2_receptions = new ArrayList<>();
    }

    public UML2_Class(
        boolean isActive        ArrayList<UML2_Reception> uml2_receptions    ) {
        this.isActive = isActive;
        this.uml2_receptions = uml2_receptions;
    }

    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public List<UML2_Reception> getUml2_receptions() {
        return uml2_receptions;
    }

    public void addUml2_reception(Uml2_reception uml2_reception) {
        this.uml2_receptions.add(uml2_reception);
    }

}