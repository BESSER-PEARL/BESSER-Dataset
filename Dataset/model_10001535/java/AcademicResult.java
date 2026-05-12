





import java.util.List;
import java.util.ArrayList;

public class AcademicResult  {

    private int semester;





    private AcademicRecords academicrecords;


    public AcademicResult(
        int semester    ) {
        this.semester = semester;
    }


    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        this.semester = semester;
    }

    public AcademicRecords getAcademicrecords() {
        return academicrecords;
    }

    public void setAcademicrecords(AcademicRecords academicrecords) {
        this.academicrecords = academicrecords;
    }

}