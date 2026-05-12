





import java.util.List;
import java.util.ArrayList;

public class JMember  {

    private String nom;





    private JObject jobject;


    public JMember(
        String nom    ) {
        this.nom = nom;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public JObject getJobject() {
        return jobject;
    }

    public void setJobject(JObject jobject) {
        this.jobject = jobject;
    }

}