





import java.util.List;
import java.util.ArrayList;

public class setup_KeyBindingContext  {

    private String iD;





    private setup_KeyBindingTask setup_keybindingtask;


    public setup_KeyBindingContext(
        String iD    ) {
        this.iD = iD;
    }


    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }

    public setup_KeyBindingTask getSetup_keybindingtask() {
        return setup_keybindingtask;
    }

    public void setSetup_keybindingtask(setup_KeyBindingTask setup_keybindingtask) {
        this.setup_keybindingtask = setup_keybindingtask;
    }

}