





import java.util.List;
import java.util.ArrayList;

public class Instruction_Interface  {






    private ProcessData processdata;




    private ProgramFileData programfiledata;


    public Instruction_Interface(
    ) {
    }



    public ProcessData getProcessdata() {
        return processdata;
    }

    public void setProcessdata(ProcessData processdata) {
        this.processdata = processdata;
    }
    public ProgramFileData getProgramfiledata() {
        return programfiledata;
    }

    public void setProgramfiledata(ProgramFileData programfiledata) {
        this.programfiledata = programfiledata;
    }

}