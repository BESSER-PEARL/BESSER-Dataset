





import java.util.List;
import java.util.ArrayList;

public class Patients  {

    private int BP;
    private int weight;
    private String name;
    private String History;
    private String Symptoms;





    private Hospital hospital;




    private Doctor doctor;


    public Patients(
        int BP,        int weight,        String name,        String History,        String Symptoms    ) {
        this.BP = BP;
        this.weight = weight;
        this.name = name;
        this.History = History;
        this.Symptoms = Symptoms;
    }


    public int getBp() {
        return BP;
    }

    public void setBp(int BP) {
        this.BP = BP;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHistory() {
        return History;
    }

    public void setHistory(String History) {
        this.History = History;
    }
    public String getSymptoms() {
        return Symptoms;
    }

    public void setSymptoms(String Symptoms) {
        this.Symptoms = Symptoms;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }
    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}