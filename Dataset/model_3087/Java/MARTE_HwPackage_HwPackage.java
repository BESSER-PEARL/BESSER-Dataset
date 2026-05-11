





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwPackage_HwPackage  {

    private int pinNum;
    private String name;
    private String packageType;





    private List<HwPackage_HwPackagePin> hwpackage_hwpackagepins;


    public MARTE_HwPackage_HwPackage(
        int pinNum,        String name,        String packageType    ) {
        this.pinNum = pinNum;
        this.name = name;
        this.packageType = packageType;
        this.hwpackage_hwpackagepins = new ArrayList<>();
    }

    public MARTE_HwPackage_HwPackage(
        int pinNum,        String name,        String packageType        ArrayList<HwPackage_HwPackagePin> hwpackage_hwpackagepins    ) {
        this.pinNum = pinNum;
        this.name = name;
        this.packageType = packageType;
        this.hwpackage_hwpackagepins = hwpackage_hwpackagepins;
    }

    public int getPinnum() {
        return pinNum;
    }

    public void setPinnum(int pinNum) {
        this.pinNum = pinNum;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPackagetype() {
        return packageType;
    }

    public void setPackagetype(String packageType) {
        this.packageType = packageType;
    }

    public List<HwPackage_HwPackagePin> getHwpackage_hwpackagepins() {
        return hwpackage_hwpackagepins;
    }

    public void addHwpackage_hwpackagepin(Hwpackage_hwpackagepin hwpackage_hwpackagepin) {
        this.hwpackage_hwpackagepins.add(hwpackage_hwpackagepin);
    }

}