





import java.util.List;
import java.util.ArrayList;

public class avm_eda_EDAModel extends SchematicModel {

    private String Library;
    private String DeviceSet;
    private String HasMultiLayerFootprint;
    private String Device;
    private String Package;



    public avm_eda_EDAModel(
        String Library,        String DeviceSet,        String HasMultiLayerFootprint,        String Device,        String Package    ) {
        super(
        );
        this.Library = Library;
        this.DeviceSet = DeviceSet;
        this.HasMultiLayerFootprint = HasMultiLayerFootprint;
        this.Device = Device;
        this.Package = Package;
    }


    public String getLibrary() {
        return Library;
    }

    public void setLibrary(String Library) {
        this.Library = Library;
    }
    public String getDeviceset() {
        return DeviceSet;
    }

    public void setDeviceset(String DeviceSet) {
        this.DeviceSet = DeviceSet;
    }
    public String getHasmultilayerfootprint() {
        return HasMultiLayerFootprint;
    }

    public void setHasmultilayerfootprint(String HasMultiLayerFootprint) {
        this.HasMultiLayerFootprint = HasMultiLayerFootprint;
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


}