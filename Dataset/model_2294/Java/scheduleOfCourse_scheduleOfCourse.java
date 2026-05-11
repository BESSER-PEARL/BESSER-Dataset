





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_scheduleOfCourse  {






    private List<scheduleOfCourse_Shift> scheduleofcourse_shifts;




    private List<scheduleOfCourse_LessonPeriod> scheduleofcourse_lessonperiods;




    private List<scheduleOfCourse_CourseLoad> scheduleofcourse_courseloads;


    public scheduleOfCourse_scheduleOfCourse(
    ) {
        this.scheduleofcourse_shifts = new ArrayList<>();
        this.scheduleofcourse_lessonperiods = new ArrayList<>();
        this.scheduleofcourse_courseloads = new ArrayList<>();
    }

    public scheduleOfCourse_scheduleOfCourse(
        ArrayList<scheduleOfCourse_Shift> scheduleofcourse_shifts,        ArrayList<scheduleOfCourse_LessonPeriod> scheduleofcourse_lessonperiods,        ArrayList<scheduleOfCourse_CourseLoad> scheduleofcourse_courseloads    ) {
        this.scheduleofcourse_shifts = scheduleofcourse_shifts;
        this.scheduleofcourse_lessonperiods = scheduleofcourse_lessonperiods;
        this.scheduleofcourse_courseloads = scheduleofcourse_courseloads;
    }


    public List<scheduleOfCourse_Shift> getScheduleofcourse_shifts() {
        return scheduleofcourse_shifts;
    }

    public void addScheduleofcourse_shift(Scheduleofcourse_shift scheduleofcourse_shift) {
        this.scheduleofcourse_shifts.add(scheduleofcourse_shift);
    }
    public List<scheduleOfCourse_LessonPeriod> getScheduleofcourse_lessonperiods() {
        return scheduleofcourse_lessonperiods;
    }

    public void addScheduleofcourse_lessonperiod(Scheduleofcourse_lessonperiod scheduleofcourse_lessonperiod) {
        this.scheduleofcourse_lessonperiods.add(scheduleofcourse_lessonperiod);
    }
    public List<scheduleOfCourse_CourseLoad> getScheduleofcourse_courseloads() {
        return scheduleofcourse_courseloads;
    }

    public void addScheduleofcourse_courseload(Scheduleofcourse_courseload scheduleofcourse_courseload) {
        this.scheduleofcourse_courseloads.add(scheduleofcourse_courseload);
    }

}