





import java.util.List;
import java.util.ArrayList;

public class oving4_EvaluationElement  {

    private float weight;
    private String type;
    private boolean attended;
    private float percentageResult;





    private oving4_Evaluation oving4_evaluation;




    private oving4_Project oving4_project;




    private oving4_Project oving4_project;


    public oving4_EvaluationElement(
        float weight,        String type,        boolean attended,        float percentageResult    ) {
        this.weight = weight;
        this.type = type;
        this.attended = attended;
        this.percentageResult = percentageResult;
    }


    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getAttended() {
        return attended;
    }

    public void setAttended(boolean attended) {
        this.attended = attended;
    }
    public float getPercentageresult() {
        return percentageResult;
    }

    public void setPercentageresult(float percentageResult) {
        this.percentageResult = percentageResult;
    }

    public oving4_Evaluation getOving4_evaluation() {
        return oving4_evaluation;
    }

    public void setOving4_evaluation(oving4_Evaluation oving4_evaluation) {
        this.oving4_evaluation = oving4_evaluation;
    }
    public oving4_Project getOving4_project() {
        return oving4_project;
    }

    public void setOving4_project(oving4_Project oving4_project) {
        this.oving4_project = oving4_project;
    }
    public oving4_Project getOving4_project() {
        return oving4_project;
    }

    public void setOving4_project(oving4_Project oving4_project) {
        this.oving4_project = oving4_project;
    }

}