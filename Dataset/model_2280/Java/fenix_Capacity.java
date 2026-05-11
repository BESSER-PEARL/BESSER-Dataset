





import java.util.List;
import java.util.ArrayList;

public class fenix_Capacity  {

    private int normal;
    private int exam;





    private fenix_CourseLoad fenix_courseload;


    public fenix_Capacity(
        int normal,        int exam    ) {
        this.normal = normal;
        this.exam = exam;
    }


    public int getNormal() {
        return normal;
    }

    public void setNormal(int normal) {
        this.normal = normal;
    }
    public int getExam() {
        return exam;
    }

    public void setExam(int exam) {
        this.exam = exam;
    }

    public fenix_CourseLoad getFenix_courseload() {
        return fenix_courseload;
    }

    public void setFenix_courseload(fenix_CourseLoad fenix_courseload) {
        this.fenix_courseload = fenix_courseload;
    }

}