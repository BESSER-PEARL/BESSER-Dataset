





import java.util.List;
import java.util.ArrayList;

public class oving4_TimeTable  {

    private boolean isRestrictedToProgramsInParallell;





    private oving4_StudyProgram oving4_studyprogram;


    public oving4_TimeTable(
        boolean isRestrictedToProgramsInParallell    ) {
        this.isRestrictedToProgramsInParallell = isRestrictedToProgramsInParallell;
    }


    public boolean getIsrestrictedtoprogramsinparallell() {
        return isRestrictedToProgramsInParallell;
    }

    public void setIsrestrictedtoprogramsinparallell(boolean isRestrictedToProgramsInParallell) {
        this.isRestrictedToProgramsInParallell = isRestrictedToProgramsInParallell;
    }

    public oving4_StudyProgram getOving4_studyprogram() {
        return oving4_studyprogram;
    }

    public void setOving4_studyprogram(oving4_StudyProgram oving4_studyprogram) {
        this.oving4_studyprogram = oving4_studyprogram;
    }

}