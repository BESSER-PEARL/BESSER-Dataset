





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeProgram  {

    private String programSection;
    private int programNo;
    private String programName;
    private String programAddress;
    private String programLenPerParam;





    private MachineLibrary_NodePrograms machinelibrary_nodeprograms;


    public MachineLibrary_NodeProgram(
        String programSection,        int programNo,        String programName,        String programAddress,        String programLenPerParam    ) {
        this.programSection = programSection;
        this.programNo = programNo;
        this.programName = programName;
        this.programAddress = programAddress;
        this.programLenPerParam = programLenPerParam;
    }


    public String getProgramsection() {
        return programSection;
    }

    public void setProgramsection(String programSection) {
        this.programSection = programSection;
    }
    public int getProgramno() {
        return programNo;
    }

    public void setProgramno(int programNo) {
        this.programNo = programNo;
    }
    public String getProgramname() {
        return programName;
    }

    public void setProgramname(String programName) {
        this.programName = programName;
    }
    public String getProgramaddress() {
        return programAddress;
    }

    public void setProgramaddress(String programAddress) {
        this.programAddress = programAddress;
    }
    public String getProgramlenperparam() {
        return programLenPerParam;
    }

    public void setProgramlenperparam(String programLenPerParam) {
        this.programLenPerParam = programLenPerParam;
    }

    public MachineLibrary_NodePrograms getMachinelibrary_nodeprograms() {
        return machinelibrary_nodeprograms;
    }

    public void setMachinelibrary_nodeprograms(MachineLibrary_NodePrograms machinelibrary_nodeprograms) {
        this.machinelibrary_nodeprograms = machinelibrary_nodeprograms;
    }

}