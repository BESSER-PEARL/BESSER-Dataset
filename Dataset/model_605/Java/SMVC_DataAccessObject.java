





import java.util.List;
import java.util.ArrayList;

public class SMVC_DataAccessObject  {

    private boolean showDirectInstancesOnly;
    private String name;





    private SMVC_SMVCApplication smvc_smvcapplication;


    public SMVC_DataAccessObject(
        boolean showDirectInstancesOnly,        String name    ) {
        this.showDirectInstancesOnly = showDirectInstancesOnly;
        this.name = name;
    }


    public boolean getShowdirectinstancesonly() {
        return showDirectInstancesOnly;
    }

    public void setShowdirectinstancesonly(boolean showDirectInstancesOnly) {
        this.showDirectInstancesOnly = showDirectInstancesOnly;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SMVC_SMVCApplication getSmvc_smvcapplication() {
        return smvc_smvcapplication;
    }

    public void setSmvc_smvcapplication(SMVC_SMVCApplication smvc_smvcapplication) {
        this.smvc_smvcapplication = smvc_smvcapplication;
    }

}