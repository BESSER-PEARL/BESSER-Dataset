





import java.util.List;
import java.util.ArrayList;

public class JMember  {

    private String nom;





    private JObject jobject;




    private JValue_Interface jvalue_interface;


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
    public JValue_Interface getJvalue_interface() {
        return jvalue_interface;
    }

    public void setJvalue_interface(JValue_Interface jvalue_interface) {
        this.jvalue_interface = jvalue_interface;
    }

}