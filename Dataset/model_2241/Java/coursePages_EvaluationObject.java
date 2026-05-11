




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class coursePages_EvaluationObject  {

    private String evaluationsForm;
    private int credits;
    private String term;
    private LocalDate date;



    public coursePages_EvaluationObject(
        String evaluationsForm,        int credits,        String term,        LocalDate date    ) {
        this.evaluationsForm = evaluationsForm;
        this.credits = credits;
        this.term = term;
        this.date = date;
    }


    public String getEvaluationsform() {
        return evaluationsForm;
    }

    public void setEvaluationsform(String evaluationsForm) {
        this.evaluationsForm = evaluationsForm;
    }
    public int getCredits() {
        return credits;
    }

    public void setCredits(int credits) {
        this.credits = credits;
    }
    public String getTerm() {
        return term;
    }

    public void setTerm(String term) {
        this.term = term;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}