





import java.util.List;
import java.util.ArrayList;

public class school_School  {






    private List<school_Pupil> school_pupils;


    public school_School(
    ) {
        this.school_pupils = new ArrayList<>();
    }

    public school_School(
        ArrayList<school_Pupil> school_pupils    ) {
        this.school_pupils = school_pupils;
    }


    public List<school_Pupil> getSchool_pupils() {
        return school_pupils;
    }

    public void addSchool_pupil(School_pupil school_pupil) {
        this.school_pupils.add(school_pupil);
    }

}