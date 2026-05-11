





import java.util.List;
import java.util.ArrayList;

public class iot_IfBlock  {






    private iot_IfStatement iot_ifstatement;




    private List<iot_AbstractElement> iot_abstractelements;




    private iot_IfStatement iot_ifstatement;


    public iot_IfBlock(
    ) {
        this.iot_abstractelements = new ArrayList<>();
    }

    public iot_IfBlock(
        ArrayList<iot_AbstractElement> iot_abstractelements    ) {
        this.iot_abstractelements = iot_abstractelements;
    }


    public iot_IfStatement getIot_ifstatement() {
        return iot_ifstatement;
    }

    public void setIot_ifstatement(iot_IfStatement iot_ifstatement) {
        this.iot_ifstatement = iot_ifstatement;
    }
    public List<iot_AbstractElement> getIot_abstractelements() {
        return iot_abstractelements;
    }

    public void addIot_abstractelement(Iot_abstractelement iot_abstractelement) {
        this.iot_abstractelements.add(iot_abstractelement);
    }
    public iot_IfStatement getIot_ifstatement() {
        return iot_ifstatement;
    }

    public void setIot_ifstatement(iot_IfStatement iot_ifstatement) {
        this.iot_ifstatement = iot_ifstatement;
    }

}