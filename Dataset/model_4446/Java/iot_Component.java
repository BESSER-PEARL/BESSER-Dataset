





import java.util.List;
import java.util.ArrayList;

public class iot_Component extends Item {






    private List<iot_ProvidedPort> iot_providedports;




    private List<iot_RequiredPort> iot_requiredports;


    public iot_Component(
    ) {
        super(
        );
        this.iot_providedports = new ArrayList<>();
        this.iot_requiredports = new ArrayList<>();
    }

    public iot_Component(
        ArrayList<iot_ProvidedPort> iot_providedports,        ArrayList<iot_RequiredPort> iot_requiredports    ) {
        this.iot_providedports = iot_providedports;
        this.iot_requiredports = iot_requiredports;
    }


    public List<iot_ProvidedPort> getIot_providedports() {
        return iot_providedports;
    }

    public void addIot_providedport(Iot_providedport iot_providedport) {
        this.iot_providedports.add(iot_providedport);
    }
    public List<iot_RequiredPort> getIot_requiredports() {
        return iot_requiredports;
    }

    public void addIot_requiredport(Iot_requiredport iot_requiredport) {
        this.iot_requiredports.add(iot_requiredport);
    }

}