





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Objective extends Element {






    private contentfwk_Objective contentfwk_objective;




    private List<contentfwk_Measure> contentfwk_measures;




    private List<contentfwk_BusinessService> contentfwk_businessservices;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Objective contentfwk_objective;




    private contentfwk_BusinessService contentfwk_businessservice;




    private contentfwk_Measure contentfwk_measure;




    private contentfwk_Goal contentfwk_goal;




    private List<contentfwk_Goal> contentfwk_goals;


    public contentfwk_Objective(
    ) {
        super(
        );
        this.contentfwk_measures = new ArrayList<>();
        this.contentfwk_businessservices = new ArrayList<>();
        this.contentfwk_goals = new ArrayList<>();
    }

    public contentfwk_Objective(
        ArrayList<contentfwk_Measure> contentfwk_measures,        ArrayList<contentfwk_BusinessService> contentfwk_businessservices,        ArrayList<contentfwk_Goal> contentfwk_goals    ) {
        this.contentfwk_measures = contentfwk_measures;
        this.contentfwk_businessservices = contentfwk_businessservices;
        this.contentfwk_goals = contentfwk_goals;
    }


    public contentfwk_Objective getContentfwk_objective() {
        return contentfwk_objective;
    }

    public void setContentfwk_objective(contentfwk_Objective contentfwk_objective) {
        this.contentfwk_objective = contentfwk_objective;
    }
    public List<contentfwk_Measure> getContentfwk_measures() {
        return contentfwk_measures;
    }

    public void addContentfwk_measure(Contentfwk_measure contentfwk_measure) {
        this.contentfwk_measures.add(contentfwk_measure);
    }
    public List<contentfwk_BusinessService> getContentfwk_businessservices() {
        return contentfwk_businessservices;
    }

    public void addContentfwk_businessservice(Contentfwk_businessservice contentfwk_businessservice) {
        this.contentfwk_businessservices.add(contentfwk_businessservice);
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Objective getContentfwk_objective() {
        return contentfwk_objective;
    }

    public void setContentfwk_objective(contentfwk_Objective contentfwk_objective) {
        this.contentfwk_objective = contentfwk_objective;
    }
    public contentfwk_BusinessService getContentfwk_businessservice() {
        return contentfwk_businessservice;
    }

    public void setContentfwk_businessservice(contentfwk_BusinessService contentfwk_businessservice) {
        this.contentfwk_businessservice = contentfwk_businessservice;
    }
    public contentfwk_Measure getContentfwk_measure() {
        return contentfwk_measure;
    }

    public void setContentfwk_measure(contentfwk_Measure contentfwk_measure) {
        this.contentfwk_measure = contentfwk_measure;
    }
    public contentfwk_Goal getContentfwk_goal() {
        return contentfwk_goal;
    }

    public void setContentfwk_goal(contentfwk_Goal contentfwk_goal) {
        this.contentfwk_goal = contentfwk_goal;
    }
    public List<contentfwk_Goal> getContentfwk_goals() {
        return contentfwk_goals;
    }

    public void addContentfwk_goal(Contentfwk_goal contentfwk_goal) {
        this.contentfwk_goals.add(contentfwk_goal);
    }

}