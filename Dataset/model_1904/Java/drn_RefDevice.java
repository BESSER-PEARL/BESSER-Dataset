





import java.util.List;
import java.util.ArrayList;

public class drn_RefDevice  {

    private String mode;





    private drn_With drn_with;




    private List<drn_Definition> drn_definitions;




    private drn_Device drn_device;


    public drn_RefDevice(
        String mode    ) {
        this.mode = mode;
        this.drn_definitions = new ArrayList<>();
    }

    public drn_RefDevice(
        String mode        ArrayList<drn_Definition> drn_definitions    ) {
        this.mode = mode;
        this.drn_definitions = drn_definitions;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public drn_With getDrn_with() {
        return drn_with;
    }

    public void setDrn_with(drn_With drn_with) {
        this.drn_with = drn_with;
    }
    public List<drn_Definition> getDrn_definitions() {
        return drn_definitions;
    }

    public void addDrn_definition(Drn_definition drn_definition) {
        this.drn_definitions.add(drn_definition);
    }
    public drn_Device getDrn_device() {
        return drn_device;
    }

    public void setDrn_device(drn_Device drn_device) {
        this.drn_device = drn_device;
    }

}