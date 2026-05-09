





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Translate_Terminal  {

    private String auto_Busy;
    private String auto_Ready;
    private String man_Busy;
    private String man_Ready;



    public MachineLibrary_Translate_Terminal(
        String auto_Busy,        String auto_Ready,        String man_Busy,        String man_Ready    ) {
        this.auto_Busy = auto_Busy;
        this.auto_Ready = auto_Ready;
        this.man_Busy = man_Busy;
        this.man_Ready = man_Ready;
    }


    public String getAuto_busy() {
        return auto_Busy;
    }

    public void setAuto_busy(String auto_Busy) {
        this.auto_Busy = auto_Busy;
    }
    public String getAuto_ready() {
        return auto_Ready;
    }

    public void setAuto_ready(String auto_Ready) {
        this.auto_Ready = auto_Ready;
    }
    public String getMan_busy() {
        return man_Busy;
    }

    public void setMan_busy(String man_Busy) {
        this.man_Busy = man_Busy;
    }
    public String getMan_ready() {
        return man_Ready;
    }

    public void setMan_ready(String man_Ready) {
        this.man_Ready = man_Ready;
    }


}