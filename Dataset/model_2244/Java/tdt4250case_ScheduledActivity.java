





import java.util.List;
import java.util.ArrayList;

public class tdt4250case_ScheduledActivity  {

    private String activity;
    private String room;
    private String timeslot;





    private List<tdt4250case_Studyprogram> tdt4250case_studyprograms;




    private tdt4250case_Timetable tdt4250case_timetable;


    public tdt4250case_ScheduledActivity(
        String activity,        String room,        String timeslot    ) {
        this.activity = activity;
        this.room = room;
        this.timeslot = timeslot;
        this.tdt4250case_studyprograms = new ArrayList<>();
    }

    public tdt4250case_ScheduledActivity(
        String activity,        String room,        String timeslot        ArrayList<tdt4250case_Studyprogram> tdt4250case_studyprograms    ) {
        this.activity = activity;
        this.room = room;
        this.timeslot = timeslot;
        this.tdt4250case_studyprograms = tdt4250case_studyprograms;
    }

    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }
    public String getTimeslot() {
        return timeslot;
    }

    public void setTimeslot(String timeslot) {
        this.timeslot = timeslot;
    }

    public List<tdt4250case_Studyprogram> getTdt4250case_studyprograms() {
        return tdt4250case_studyprograms;
    }

    public void addTdt4250case_studyprogram(Tdt4250case_studyprogram tdt4250case_studyprogram) {
        this.tdt4250case_studyprograms.add(tdt4250case_studyprogram);
    }
    public tdt4250case_Timetable getTdt4250case_timetable() {
        return tdt4250case_timetable;
    }

    public void setTdt4250case_timetable(tdt4250case_Timetable tdt4250case_timetable) {
        this.tdt4250case_timetable = tdt4250case_timetable;
    }

}