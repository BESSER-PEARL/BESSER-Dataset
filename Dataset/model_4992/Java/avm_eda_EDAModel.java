





import java.util.List;
import java.util.ArrayList;

public class avm_eda_EDAModel extends SchematicModel {

    private String HasMultiLayerFootprint;
    private String DeviceSet;
    private String Device;
    private String Package;
    private String Library;





    private List<eda_Parameter> eda_parameters;


    public avm_eda_EDAModel(
        String HasMultiLayerFootprint,        String DeviceSet,        String Device,        String Package,        String Library    ) {
        super(
        );
        this.HasMultiLayerFootprint = HasMultiLayerFootprint;
        this.DeviceSet = DeviceSet;
        this.Device = Device;
        this.Package = Package;
        this.Library = Library;
        this.eda_parameters = new ArrayList<>();
    }

    public avm_eda_EDAModel(
        String HasMultiLayerFootprint,        String DeviceSet,        String Device,        String Package,        String Library        ArrayList<eda_Parameter> eda_parameters    ) {
        this.HasMultiLayerFootprint = HasMultiLayerFootprint;
        this.DeviceSet = DeviceSet;
        this.Device = Device;
        this.Package = Package;
        this.Library = Library;
        this.eda_parameters = eda_parameters;
    }

    public String getHasmultilayerfootprint() {
        return HasMultiLayerFootprint;
    }

    public void setHasmultilayerfootprint(String HasMultiLayerFootprint) {
        this.HasMultiLayerFootprint = HasMultiLayerFootprint;
    }
    public String getDeviceset() {
        return DeviceSet;
    }

    public void setDeviceset(String DeviceSet) {
        this.DeviceSet = DeviceSet;
    }
    public String getDevice() {
        return Device;
    }

    public void setDevice(String Device) {
        this.Device = Device;
    }
    public String getPackage() {
        return Package;
    }

    public void setPackage(String Package) {
        this.Package = Package;
    }
    public String getLibrary() {
        return Library;
    }

    public void setLibrary(String Library) {
        this.Library = Library;
    }

    public List<eda_Parameter> getEda_parameters() {
        return eda_parameters;
    }

    public void addEda_parameter(Eda_parameter eda_parameter) {
        this.eda_parameters.add(eda_parameter);
    }

}