





import java.util.List;
import java.util.ArrayList;

public class oving4_CourseInstance  {

    private int sumLectureHours;
    private int sumInDepthHours;
    private int sumExerciseHours;





    private oving4_TimeTable oving4_timetable;




    private oving4_PersonRole oving4_personrole;




    private List<oving4_CourseWork> oving4_courseworks;




    private List<oving4_Evaluation> oving4_evaluations;




    private oving4_Evaluation oving4_evaluation;




    private oving4_Course oving4_course;




    private oving4_Course oving4_course;




    private oving4_TimeTable oving4_timetable;




    private List<oving4_PersonRole> oving4_personroles;


    public oving4_CourseInstance(
        int sumLectureHours,        int sumInDepthHours,        int sumExerciseHours    ) {
        this.sumLectureHours = sumLectureHours;
        this.sumInDepthHours = sumInDepthHours;
        this.sumExerciseHours = sumExerciseHours;
        this.oving4_courseworks = new ArrayList<>();
        this.oving4_evaluations = new ArrayList<>();
        this.oving4_personroles = new ArrayList<>();
    }

    public oving4_CourseInstance(
        int sumLectureHours,        int sumInDepthHours,        int sumExerciseHours        ArrayList<oving4_CourseWork> oving4_courseworks,        ArrayList<oving4_Evaluation> oving4_evaluations,        ArrayList<oving4_PersonRole> oving4_personroles    ) {
        this.sumLectureHours = sumLectureHours;
        this.sumInDepthHours = sumInDepthHours;
        this.sumExerciseHours = sumExerciseHours;
        this.oving4_courseworks = oving4_courseworks;
        this.oving4_evaluations = oving4_evaluations;
        this.oving4_personroles = oving4_personroles;
    }

    public int getSumlecturehours() {
        return sumLectureHours;
    }

    public void setSumlecturehours(int sumLectureHours) {
        this.sumLectureHours = sumLectureHours;
    }
    public int getSumindepthhours() {
        return sumInDepthHours;
    }

    public void setSumindepthhours(int sumInDepthHours) {
        this.sumInDepthHours = sumInDepthHours;
    }
    public int getSumexercisehours() {
        return sumExerciseHours;
    }

    public void setSumexercisehours(int sumExerciseHours) {
        this.sumExerciseHours = sumExerciseHours;
    }

    public oving4_TimeTable getOving4_timetable() {
        return oving4_timetable;
    }

    public void setOving4_timetable(oving4_TimeTable oving4_timetable) {
        this.oving4_timetable = oving4_timetable;
    }
    public oving4_PersonRole getOving4_personrole() {
        return oving4_personrole;
    }

    public void setOving4_personrole(oving4_PersonRole oving4_personrole) {
        this.oving4_personrole = oving4_personrole;
    }
    public List<oving4_CourseWork> getOving4_courseworks() {
        return oving4_courseworks;
    }

    public void addOving4_coursework(Oving4_coursework oving4_coursework) {
        this.oving4_courseworks.add(oving4_coursework);
    }
    public List<oving4_Evaluation> getOving4_evaluations() {
        return oving4_evaluations;
    }

    public void addOving4_evaluation(Oving4_evaluation oving4_evaluation) {
        this.oving4_evaluations.add(oving4_evaluation);
    }
    public oving4_Evaluation getOving4_evaluation() {
        return oving4_evaluation;
    }

    public void setOving4_evaluation(oving4_Evaluation oving4_evaluation) {
        this.oving4_evaluation = oving4_evaluation;
    }
    public oving4_Course getOving4_course() {
        return oving4_course;
    }

    public void setOving4_course(oving4_Course oving4_course) {
        this.oving4_course = oving4_course;
    }
    public oving4_Course getOving4_course() {
        return oving4_course;
    }

    public void setOving4_course(oving4_Course oving4_course) {
        this.oving4_course = oving4_course;
    }
    public oving4_TimeTable getOving4_timetable() {
        return oving4_timetable;
    }

    public void setOving4_timetable(oving4_TimeTable oving4_timetable) {
        this.oving4_timetable = oving4_timetable;
    }
    public List<oving4_PersonRole> getOving4_personroles() {
        return oving4_personroles;
    }

    public void addOving4_personrole(Oving4_personrole oving4_personrole) {
        this.oving4_personroles.add(oving4_personrole);
    }

}