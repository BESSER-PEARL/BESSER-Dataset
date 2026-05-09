





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_miniOCL_PackageCS  {

    private None name;





    private List<PackageCS> packagecss;


    public mutatorenvironment_miniOCL_PackageCS(
        None name    ) {
        this.name = name;
        this.packagecss = new ArrayList<>();
    }

    public mutatorenvironment_miniOCL_PackageCS(
        None name        ArrayList<PackageCS> packagecss    ) {
        this.name = name;
        this.packagecss = packagecss;
    }

    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }

    public List<PackageCS> getPackagecss() {
        return packagecss;
    }

    public void addPackagecs(Packagecs packagecs) {
        this.packagecss.add(packagecs);
    }

}