





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_GeneralParameter_SuperQXRF  {

    private String switchRemote;
    private String listName;
    private String startList;



    public MachineLibrary_GeneralParameter_SuperQXRF(
        String switchRemote,        String listName,        String startList    ) {
        this.switchRemote = switchRemote;
        this.listName = listName;
        this.startList = startList;
    }


    public String getSwitchremote() {
        return switchRemote;
    }

    public void setSwitchremote(String switchRemote) {
        this.switchRemote = switchRemote;
    }
    public String getListname() {
        return listName;
    }

    public void setListname(String listName) {
        this.listName = listName;
    }
    public String getStartlist() {
        return startList;
    }

    public void setStartlist(String startList) {
        this.startList = startList;
    }


}