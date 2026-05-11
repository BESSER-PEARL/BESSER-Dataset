





import java.util.List;
import java.util.ArrayList;

public class fenix_scheduleOfCourse  {






    private List<fenix_Shift> fenix_shifts;




    private List<fenix_LessonPeriod> fenix_lessonperiods;




    private List<fenix_CourseLoad> fenix_courseloads;


    public fenix_scheduleOfCourse(
    ) {
        this.fenix_shifts = new ArrayList<>();
        this.fenix_lessonperiods = new ArrayList<>();
        this.fenix_courseloads = new ArrayList<>();
    }

    public fenix_scheduleOfCourse(
        ArrayList<fenix_Shift> fenix_shifts,        ArrayList<fenix_LessonPeriod> fenix_lessonperiods,        ArrayList<fenix_CourseLoad> fenix_courseloads    ) {
        this.fenix_shifts = fenix_shifts;
        this.fenix_lessonperiods = fenix_lessonperiods;
        this.fenix_courseloads = fenix_courseloads;
    }


    public List<fenix_Shift> getFenix_shifts() {
        return fenix_shifts;
    }

    public void addFenix_shift(Fenix_shift fenix_shift) {
        this.fenix_shifts.add(fenix_shift);
    }
    public List<fenix_LessonPeriod> getFenix_lessonperiods() {
        return fenix_lessonperiods;
    }

    public void addFenix_lessonperiod(Fenix_lessonperiod fenix_lessonperiod) {
        this.fenix_lessonperiods.add(fenix_lessonperiod);
    }
    public List<fenix_CourseLoad> getFenix_courseloads() {
        return fenix_courseloads;
    }

    public void addFenix_courseload(Fenix_courseload fenix_courseload) {
        this.fenix_courseloads.add(fenix_courseload);
    }

}