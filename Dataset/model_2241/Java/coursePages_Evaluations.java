





import java.util.List;
import java.util.ArrayList;

public class coursePages_Evaluations  {






    private List<coursePages_EvaluationObject> coursepages_evaluationobjects;


    public coursePages_Evaluations(
    ) {
        this.coursepages_evaluationobjects = new ArrayList<>();
    }

    public coursePages_Evaluations(
        ArrayList<coursePages_EvaluationObject> coursepages_evaluationobjects    ) {
        this.coursepages_evaluationobjects = coursepages_evaluationobjects;
    }


    public List<coursePages_EvaluationObject> getCoursepages_evaluationobjects() {
        return coursepages_evaluationobjects;
    }

    public void addCoursepages_evaluationobject(Coursepages_evaluationobject coursepages_evaluationobject) {
        this.coursepages_evaluationobjects.add(coursepages_evaluationobject);
    }

}