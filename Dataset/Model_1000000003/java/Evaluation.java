





import java.util.List;
import java.util.ArrayList;

public class Evaluation  {

    private None status;





    private List<Observation> observations;




    private Element element;




    private Configuration configuration;




    private Project project;




    private List<Element> elements;


    public Evaluation(
        None status    ) {
        this.status = status;
        this.observations = new ArrayList<>();
        this.elements = new ArrayList<>();
    }

    public Evaluation(
        None status        ArrayList<Observation> observations,        ArrayList<Element> elements    ) {
        this.status = status;
        this.observations = observations;
        this.elements = elements;
    }

    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }

    public List<Observation> getObservations() {
        return observations;
    }

    public void addObservation(Observation observation) {
        this.observations.add(observation);
    }
    public Element getElement() {
        return element;
    }

    public void setElement(Element element) {
        this.element = element;
    }
    public Configuration getConfiguration() {
        return configuration;
    }

    public void setConfiguration(Configuration configuration) {
        this.configuration = configuration;
    }
    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }
    public List<Element> getElements() {
        return elements;
    }

    public void addElement(Element element) {
        this.elements.add(element);
    }

}