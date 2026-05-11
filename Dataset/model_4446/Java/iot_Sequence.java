





import java.util.List;
import java.util.ArrayList;

public class iot_Sequence extends Controller {






    private List<iot_RequiredPort> iot_requiredports;


    public iot_Sequence(
    ) {
        super(
        );
        this.iot_requiredports = new ArrayList<>();
    }

    public iot_Sequence(
        ArrayList<iot_RequiredPort> iot_requiredports    ) {
        this.iot_requiredports = iot_requiredports;
    }


    public List<iot_RequiredPort> getIot_requiredports() {
        return iot_requiredports;
    }

    public void addIot_requiredport(Iot_requiredport iot_requiredport) {
        this.iot_requiredports.add(iot_requiredport);
    }

}