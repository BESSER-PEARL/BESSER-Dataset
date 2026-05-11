





import java.util.List;
import java.util.ArrayList;

public class tdt4250case_ExaminationActivity  {

    private String weighting;
    private String evaluationForm;





    private tdt4250case_Examination tdt4250case_examination;


    public tdt4250case_ExaminationActivity(
        String weighting,        String evaluationForm    ) {
        this.weighting = weighting;
        this.evaluationForm = evaluationForm;
    }


    public String getWeighting() {
        return weighting;
    }

    public void setWeighting(String weighting) {
        this.weighting = weighting;
    }
    public String getEvaluationform() {
        return evaluationForm;
    }

    public void setEvaluationform(String evaluationForm) {
        this.evaluationForm = evaluationForm;
    }

    public tdt4250case_Examination getTdt4250case_examination() {
        return tdt4250case_examination;
    }

    public void setTdt4250case_examination(tdt4250case_Examination tdt4250case_examination) {
        this.tdt4250case_examination = tdt4250case_examination;
    }

}