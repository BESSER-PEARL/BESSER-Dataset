





import java.util.List;
import java.util.ArrayList;

public class training_TrainingOrganization  {

    private String name;





    private List<training_Person> training_persons;


    public training_TrainingOrganization(
        String name    ) {
        this.name = name;
        this.training_persons = new ArrayList<>();
    }

    public training_TrainingOrganization(
        String name        ArrayList<training_Person> training_persons    ) {
        this.name = name;
        this.training_persons = training_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<training_Person> getTraining_persons() {
        return training_persons;
    }

    public void addTraining_person(Training_person training_person) {
        this.training_persons.add(training_person);
    }

}