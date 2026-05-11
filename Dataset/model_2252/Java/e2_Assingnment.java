




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class e2_Assingnment  {

    private String Content;
    private String Type;
    private LocalDate StartDate;
    private LocalDate Deadline;
    private String Title;
    private boolean isMandatory;





    private e2_LectureContent e2_lecturecontent;




    private List<e2_SubGoal> e2_subgoals;




    private e2_Course e2_course;




    private e2_AssignmentSubmission e2_assignmentsubmission;


    public e2_Assingnment(
        String Content,        String Type,        LocalDate StartDate,        LocalDate Deadline,        String Title,        boolean isMandatory    ) {
        this.Content = Content;
        this.Type = Type;
        this.StartDate = StartDate;
        this.Deadline = Deadline;
        this.Title = Title;
        this.isMandatory = isMandatory;
        this.e2_subgoals = new ArrayList<>();
    }

    public e2_Assingnment(
        String Content,        String Type,        LocalDate StartDate,        LocalDate Deadline,        String Title,        boolean isMandatory        ArrayList<e2_SubGoal> e2_subgoals    ) {
        this.Content = Content;
        this.Type = Type;
        this.StartDate = StartDate;
        this.Deadline = Deadline;
        this.Title = Title;
        this.isMandatory = isMandatory;
        this.e2_subgoals = e2_subgoals;
    }

    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public LocalDate getStartdate() {
        return StartDate;
    }

    public void setStartdate(LocalDate StartDate) {
        this.StartDate = StartDate;
    }
    public LocalDate getDeadline() {
        return Deadline;
    }

    public void setDeadline(LocalDate Deadline) {
        this.Deadline = Deadline;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }

    public e2_LectureContent getE2_lecturecontent() {
        return e2_lecturecontent;
    }

    public void setE2_lecturecontent(e2_LectureContent e2_lecturecontent) {
        this.e2_lecturecontent = e2_lecturecontent;
    }
    public List<e2_SubGoal> getE2_subgoals() {
        return e2_subgoals;
    }

    public void addE2_subgoal(E2_subgoal e2_subgoal) {
        this.e2_subgoals.add(e2_subgoal);
    }
    public e2_Course getE2_course() {
        return e2_course;
    }

    public void setE2_course(e2_Course e2_course) {
        this.e2_course = e2_course;
    }
    public e2_AssignmentSubmission getE2_assignmentsubmission() {
        return e2_assignmentsubmission;
    }

    public void setE2_assignmentsubmission(e2_AssignmentSubmission e2_assignmentsubmission) {
        this.e2_assignmentsubmission = e2_assignmentsubmission;
    }

}