





import java.util.List;
import java.util.ArrayList;

public class ra_Semester  {

    private int semesterNumber;
    private float totalPoints;



    public ra_Semester(
        int semesterNumber,        float totalPoints    ) {
        this.semesterNumber = semesterNumber;
        this.totalPoints = totalPoints;
    }


    public int getSemesternumber() {
        return semesterNumber;
    }

    public void setSemesternumber(int semesterNumber) {
        this.semesterNumber = semesterNumber;
    }
    public float getTotalpoints() {
        return totalPoints;
    }

    public void setTotalpoints(float totalPoints) {
        this.totalPoints = totalPoints;
    }


}