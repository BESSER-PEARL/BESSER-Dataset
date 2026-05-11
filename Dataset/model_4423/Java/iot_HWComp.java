





import java.util.List;
import java.util.ArrayList;

public class iot_HWComp  {

    private String name;





    private List<iot_IotOperationDef> iot_iotoperationdefs;


    public iot_HWComp(
        String name    ) {
        this.name = name;
        this.iot_iotoperationdefs = new ArrayList<>();
    }

    public iot_HWComp(
        String name        ArrayList<iot_IotOperationDef> iot_iotoperationdefs    ) {
        this.name = name;
        this.iot_iotoperationdefs = iot_iotoperationdefs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<iot_IotOperationDef> getIot_iotoperationdefs() {
        return iot_iotoperationdefs;
    }

    public void addIot_iotoperationdef(Iot_iotoperationdef iot_iotoperationdef) {
        this.iot_iotoperationdefs.add(iot_iotoperationdef);
    }

}