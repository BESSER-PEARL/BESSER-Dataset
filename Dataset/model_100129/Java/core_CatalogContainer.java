





import java.util.List;
import java.util.ArrayList;

public class core_CatalogContainer  {

    private boolean supportsGuestAccess;
    private boolean active;
    private String name;





    private core_ConnectionConfig core_connectionconfig;


    public core_CatalogContainer(
        boolean supportsGuestAccess,        boolean active,        String name    ) {
        this.supportsGuestAccess = supportsGuestAccess;
        this.active = active;
        this.name = name;
    }


    public boolean getSupportsguestaccess() {
        return supportsGuestAccess;
    }

    public void setSupportsguestaccess(boolean supportsGuestAccess) {
        this.supportsGuestAccess = supportsGuestAccess;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public core_ConnectionConfig getCore_connectionconfig() {
        return core_connectionconfig;
    }

    public void setCore_connectionconfig(core_ConnectionConfig core_connectionconfig) {
        this.core_connectionconfig = core_connectionconfig;
    }

}