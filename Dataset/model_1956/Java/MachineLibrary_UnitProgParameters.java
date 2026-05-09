





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitProgParameters  {

    private int parameterNo;
    private String parameter;





    private MachineLibrary_UnitProgram machinelibrary_unitprogram;


    public MachineLibrary_UnitProgParameters(
        int parameterNo,        String parameter    ) {
        this.parameterNo = parameterNo;
        this.parameter = parameter;
    }


    public int getParameterno() {
        return parameterNo;
    }

    public void setParameterno(int parameterNo) {
        this.parameterNo = parameterNo;
    }
    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }

    public MachineLibrary_UnitProgram getMachinelibrary_unitprogram() {
        return machinelibrary_unitprogram;
    }

    public void setMachinelibrary_unitprogram(MachineLibrary_UnitProgram machinelibrary_unitprogram) {
        this.machinelibrary_unitprogram = machinelibrary_unitprogram;
    }

}