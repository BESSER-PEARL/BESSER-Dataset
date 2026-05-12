





import java.util.List;
import java.util.ArrayList;

public class core_CatalogContainer  {

    private boolean active;
    private String name;
    private boolean supportsGuestAccess;



    public core_CatalogContainer(
        boolean active,        String name,        boolean supportsGuestAccess    ) {
        this.active = active;
        this.name = name;
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
    public boolean getSupportsguestaccess() {
        return supportsGuestAccess;
    }

    public void setSupportsguestaccess(boolean supportsGuestAccess) {
        this.supportsGuestAccess = supportsGuestAccess;
    }


}