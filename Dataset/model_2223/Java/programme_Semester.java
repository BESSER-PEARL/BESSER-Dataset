





import java.util.List;
import java.util.ArrayList;

public class programme_Semester  {

    private String semesterType;





    private programme_StudyYear programme_studyyear;


    public programme_Semester(
        String semesterType    ) {
        this.semesterType = semesterType;
    }


    public String getSemestertype() {
        return semesterType;
    }

    public void setSemestertype(String semesterType) {
        this.semesterType = semesterType;
    }

    public programme_StudyYear getProgramme_studyyear() {
        return programme_studyyear;
    }

    public void setProgramme_studyyear(programme_StudyYear programme_studyyear) {
        this.programme_studyyear = programme_studyyear;
    }

}