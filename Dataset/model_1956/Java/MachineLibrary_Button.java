





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Button  {

    private String buttonText;
    private int buttonNo;
    private int commandNo;





    private MachineLibrary_Buttons machinelibrary_buttons;


    public MachineLibrary_Button(
        String buttonText,        int buttonNo,        int commandNo    ) {
        this.buttonText = buttonText;
        this.buttonNo = buttonNo;
        this.commandNo = commandNo;
    }


    public String getButtontext() {
        return buttonText;
    }

    public void setButtontext(String buttonText) {
        this.buttonText = buttonText;
    }
    public int getButtonno() {
        return buttonNo;
    }

    public void setButtonno(int buttonNo) {
        this.buttonNo = buttonNo;
    }
    public int getCommandno() {
        return commandNo;
    }

    public void setCommandno(int commandNo) {
        this.commandNo = commandNo;
    }

    public MachineLibrary_Buttons getMachinelibrary_buttons() {
        return machinelibrary_buttons;
    }

    public void setMachinelibrary_buttons(MachineLibrary_Buttons machinelibrary_buttons) {
        this.machinelibrary_buttons = machinelibrary_buttons;
    }

}