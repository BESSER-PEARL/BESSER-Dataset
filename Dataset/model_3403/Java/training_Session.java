




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class training_Session  {

    private LocalDate date;





    private training_Trainer training_trainer;




    private List<training_Person> training_persons;




    private training_TrainingOrganization training_trainingorganization;


    public training_Session(
        LocalDate date    ) {
        this.date = date;
        this.training_persons = new ArrayList<>();
    }

    public training_Session(
        LocalDate date        ArrayList<training_Person> training_persons    ) {
        this.date = date;
        this.training_persons = training_persons;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public training_Trainer getTraining_trainer() {
        return training_trainer;
    }

    public void setTraining_trainer(training_Trainer training_trainer) {
        this.training_trainer = training_trainer;
    }
    public List<training_Person> getTraining_persons() {
        return training_persons;
    }

    public void addTraining_person(Training_person training_person) {
        this.training_persons.add(training_person);
    }
    public training_TrainingOrganization getTraining_trainingorganization() {
        return training_trainingorganization;
    }

    public void setTraining_trainingorganization(training_TrainingOrganization training_trainingorganization) {
        this.training_trainingorganization = training_trainingorganization;
    }

}