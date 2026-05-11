




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Delivery  {

    private LocalDate submission_date;
    private int group_number;
    private String answer;
    private int ID;





    private model_Student model_student;


    public model_Delivery(
        LocalDate submission_date,        int group_number,        String answer,        int ID    ) {
        this.submission_date = submission_date;
        this.group_number = group_number;
        this.answer = answer;
        this.ID = ID;
    }


    public LocalDate getSubmission_date() {
        return submission_date;
    }

    public void setSubmission_date(LocalDate submission_date) {
        this.submission_date = submission_date;
    }
    public int getGroup_number() {
        return group_number;
    }

    public void setGroup_number(int group_number) {
        this.group_number = group_number;
    }
    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public model_Student getModel_student() {
        return model_student;
    }

    public void setModel_student(model_Student model_student) {
        this.model_student = model_student;
    }

}