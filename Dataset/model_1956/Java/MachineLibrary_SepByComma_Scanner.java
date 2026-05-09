





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_SepByComma_Scanner  {

    private int preDefWS;
    private int activ;





    private MachineLibrary_UnitSpecialConfiguration machinelibrary_unitspecialconfiguration;


    public MachineLibrary_SepByComma_Scanner(
        int preDefWS,        int activ    ) {
        this.preDefWS = preDefWS;
        this.activ = activ;
    }


    public int getPredefws() {
        return preDefWS;
    }

    public void setPredefws(int preDefWS) {
        this.preDefWS = preDefWS;
    }
    public int getActiv() {
        return activ;
    }

    public void setActiv(int activ) {
        this.activ = activ;
    }

    public MachineLibrary_UnitSpecialConfiguration getMachinelibrary_unitspecialconfiguration() {
        return machinelibrary_unitspecialconfiguration;
    }

    public void setMachinelibrary_unitspecialconfiguration(MachineLibrary_UnitSpecialConfiguration machinelibrary_unitspecialconfiguration) {
        this.machinelibrary_unitspecialconfiguration = machinelibrary_unitspecialconfiguration;
    }

}