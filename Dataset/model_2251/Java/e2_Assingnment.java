




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class e2_Assingnment  {

    private boolean isMandatory;
    private LocalDate StartDate;
    private String Content;
    private LocalDate Deadline;
    private String Type;
    private String Title;





    private e2_AssignmentSubmission e2_assignmentsubmission;




    private e2_LectureContent e2_lecturecontent;


    public e2_Assingnment(
        boolean isMandatory,        LocalDate StartDate,        String Content,        LocalDate Deadline,        String Type,        String Title    ) {
        this.isMandatory = isMandatory;
        this.StartDate = StartDate;
        this.Content = Content;
        this.Deadline = Deadline;
        this.Type = Type;
        this.Title = Title;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public LocalDate getStartdate() {
        return StartDate;
    }

    public void setStartdate(LocalDate StartDate) {
        this.StartDate = StartDate;
    }
    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }
    public LocalDate getDeadline() {
        return Deadline;
    }

    public void setDeadline(LocalDate Deadline) {
        this.Deadline = Deadline;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }

    public e2_AssignmentSubmission getE2_assignmentsubmission() {
        return e2_assignmentsubmission;
    }

    public void setE2_assignmentsubmission(e2_AssignmentSubmission e2_assignmentsubmission) {
        this.e2_assignmentsubmission = e2_assignmentsubmission;
    }
    public e2_LectureContent getE2_lecturecontent() {
        return e2_lecturecontent;
    }

    public void setE2_lecturecontent(e2_LectureContent e2_lecturecontent) {
        this.e2_lecturecontent = e2_lecturecontent;
    }

}