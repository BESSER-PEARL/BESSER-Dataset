





import java.util.List;
import java.util.ArrayList;

public class SMVC_DataAccessObject  {

    private String name;
    private boolean showDirectInstancesOnly;





    private SMVC_EntityController smvc_entitycontroller;




    private SMVC_SMVCApplication smvc_smvcapplication;


    public SMVC_DataAccessObject(
        String name,        boolean showDirectInstancesOnly    ) {
        this.name = name;
        this.showDirectInstancesOnly = showDirectInstancesOnly;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getShowdirectinstancesonly() {
        return showDirectInstancesOnly;
    }

    public void setShowdirectinstancesonly(boolean showDirectInstancesOnly) {
        this.showDirectInstancesOnly = showDirectInstancesOnly;
    }

    public SMVC_EntityController getSmvc_entitycontroller() {
        return smvc_entitycontroller;
    }

    public void setSmvc_entitycontroller(SMVC_EntityController smvc_entitycontroller) {
        this.smvc_entitycontroller = smvc_entitycontroller;
    }
    public SMVC_SMVCApplication getSmvc_smvcapplication() {
        return smvc_smvcapplication;
    }

    public void setSmvc_smvcapplication(SMVC_SMVCApplication smvc_smvcapplication) {
        this.smvc_smvcapplication = smvc_smvcapplication;
    }

}