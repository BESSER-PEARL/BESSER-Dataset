





import java.util.List;
import java.util.ArrayList;

public class setup_CommandParameter  {

    private String iD;
    private String value;





    private setup_KeyBindingTask setup_keybindingtask;


    public setup_CommandParameter(
        String iD,        String value    ) {
        this.iD = iD;
        this.value = value;
    }


    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public setup_KeyBindingTask getSetup_keybindingtask() {
        return setup_keybindingtask;
    }

    public void setSetup_keybindingtask(setup_KeyBindingTask setup_keybindingtask) {
        this.setup_keybindingtask = setup_keybindingtask;
    }

}