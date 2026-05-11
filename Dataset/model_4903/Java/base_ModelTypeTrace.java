





import java.util.List;
import java.util.ArrayList;

public class base_ModelTypeTrace extends IdElement {

    private String name;





    private base_AllInstancesAccess base_allinstancesaccess;


    public base_ModelTypeTrace(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public base_AllInstancesAccess getBase_allinstancesaccess() {
        return base_allinstancesaccess;
    }

    public void setBase_allinstancesaccess(base_AllInstancesAccess base_allinstancesaccess) {
        this.base_allinstancesaccess = base_allinstancesaccess;
    }

}