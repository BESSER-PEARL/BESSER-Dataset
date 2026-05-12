





import java.util.List;
import java.util.ArrayList;

public class lab  {

    private int price;
    private String results;





    private Doctor doctor;




    private Patient patient;


    public lab(
        int price,        String results    ) {
        this.price = price;
        this.results = results;
    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getResults() {
        return results;
    }

    public void setResults(String results) {
        this.results = results;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}