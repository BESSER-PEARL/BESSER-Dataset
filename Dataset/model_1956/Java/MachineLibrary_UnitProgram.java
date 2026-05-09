





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitProgram  {

    private String unitProgName;





    private MachineLibrary_UnitPrograms machinelibrary_unitprograms;


    public MachineLibrary_UnitProgram(
        String unitProgName    ) {
        this.unitProgName = unitProgName;
    }


    public String getUnitprogname() {
        return unitProgName;
    }

    public void setUnitprogname(String unitProgName) {
        this.unitProgName = unitProgName;
    }

    public MachineLibrary_UnitPrograms getMachinelibrary_unitprograms() {
        return machinelibrary_unitprograms;
    }

    public void setMachinelibrary_unitprograms(MachineLibrary_UnitPrograms machinelibrary_unitprograms) {
        this.machinelibrary_unitprograms = machinelibrary_unitprograms;
    }

}