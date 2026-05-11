





import java.util.List;
import java.util.ArrayList;

public class spinefm_SystemActionModel_ActionAbstractRename extends SystemAction {

    private String oldName;
    private String newName;



    public spinefm_SystemActionModel_ActionAbstractRename(
        String oldName,        String newName    ) {
        super(
        );
        this.oldName = oldName;
        this.newName = newName;
    }


    public String getOldname() {
        return oldName;
    }

    public void setOldname(String oldName) {
        this.oldName = oldName;
    }
    public String getNewname() {
        return newName;
    }

    public void setNewname(String newName) {
        this.newName = newName;
    }


}