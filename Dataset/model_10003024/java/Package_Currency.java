





import java.util.List;
import java.util.ArrayList;

public class Package_Currency  {

    private String id;
    private String name;
    private String abr;





    private Package_Bill package_bill;


    public Package_Currency(
        String id,        String name,        String abr    ) {
        this.id = id;
        this.name = name;
        this.abr = abr;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAbr() {
        return abr;
    }

    public void setAbr(String abr) {
        this.abr = abr;
    }

    public Package_Bill getPackage_bill() {
        return package_bill;
    }

    public void setPackage_bill(Package_Bill package_bill) {
        this.package_bill = package_bill;
    }

}