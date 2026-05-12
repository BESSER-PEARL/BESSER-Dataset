





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private String HTID;





    private Manager manager;




    private Admin admin;




    private Hub_Device hub_device;


    public Users(
        String HTID    ) {
        this.HTID = HTID;
    }


    public String getHtid() {
        return HTID;
    }

    public void setHtid(String HTID) {
        this.HTID = HTID;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Hub_Device getHub_device() {
        return hub_device;
    }

    public void setHub_device(Hub_Device hub_device) {
        this.hub_device = hub_device;
    }

}