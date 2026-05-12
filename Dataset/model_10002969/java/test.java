





import java.util.List;
import java.util.ArrayList;

public class test  {

    private String disease_name;





    private doctor doctor;


    public test(
        String disease_name    ) {
        this.disease_name = disease_name;
    }


    public String getDisease_name() {
        return disease_name;
    }

    public void setDisease_name(String disease_name) {
        this.disease_name = disease_name;
    }

    public doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(doctor doctor) {
        this.doctor = doctor;
    }

}