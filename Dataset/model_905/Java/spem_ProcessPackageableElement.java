





import java.util.List;
import java.util.ArrayList;

public class spem_ProcessPackageableElement  {

    private String name;





    private spem_ProcessPackage spem_processpackage;


    public spem_ProcessPackageableElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public spem_ProcessPackage getSpem_processpackage() {
        return spem_processpackage;
    }

    public void setSpem_processpackage(spem_ProcessPackage spem_processpackage) {
        this.spem_processpackage = spem_processpackage;
    }

}