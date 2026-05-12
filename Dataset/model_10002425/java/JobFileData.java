





import java.util.List;
import java.util.ArrayList;

public class JobFileData  {

    private None programs;
    private None startTimes;





    private ProgramFileData programfiledata;


    public JobFileData(
        None programs,        None startTimes    ) {
        this.programs = programs;
        this.startTimes = startTimes;
    }


    public None getPrograms() {
        return programs;
    }

    public void setPrograms(None programs) {
        this.programs = programs;
    }
    public None getStarttimes() {
        return startTimes;
    }

    public void setStarttimes(None startTimes) {
        this.startTimes = startTimes;
    }

    public ProgramFileData getProgramfiledata() {
        return programfiledata;
    }

    public void setProgramfiledata(ProgramFileData programfiledata) {
        this.programfiledata = programfiledata;
    }

}