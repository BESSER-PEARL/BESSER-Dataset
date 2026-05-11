





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_DataStreams  {






    private List<ioT_metamodel_AtomicData> iot_metamodel_atomicdatas;




    private ioT_metamodel_Information iot_metamodel_information;


    public ioT_metamodel_DataStreams(
    ) {
        this.iot_metamodel_atomicdatas = new ArrayList<>();
    }

    public ioT_metamodel_DataStreams(
        ArrayList<ioT_metamodel_AtomicData> iot_metamodel_atomicdatas    ) {
        this.iot_metamodel_atomicdatas = iot_metamodel_atomicdatas;
    }


    public List<ioT_metamodel_AtomicData> getIot_metamodel_atomicdatas() {
        return iot_metamodel_atomicdatas;
    }

    public void addIot_metamodel_atomicdata(Iot_metamodel_atomicdata iot_metamodel_atomicdata) {
        this.iot_metamodel_atomicdatas.add(iot_metamodel_atomicdata);
    }
    public ioT_metamodel_Information getIot_metamodel_information() {
        return iot_metamodel_information;
    }

    public void setIot_metamodel_information(ioT_metamodel_Information iot_metamodel_information) {
        this.iot_metamodel_information = iot_metamodel_information;
    }

}