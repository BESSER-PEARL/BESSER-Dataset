





import java.util.List;
import java.util.ArrayList;

public class SMVC_Entity  {

    private String name;





    private SMVC_SMVCApplication smvc_smvcapplication;




    private SMVC_DataAccessObject smvc_dataaccessobject;


    public SMVC_Entity(
        String name    ) {
        this.name = name;
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
    public SMVC_DataAccessObject getSmvc_dataaccessobject() {
        return smvc_dataaccessobject;
    }

    public void setSmvc_dataaccessobject(SMVC_DataAccessObject smvc_dataaccessobject) {
        this.smvc_dataaccessobject = smvc_dataaccessobject;
    }

}