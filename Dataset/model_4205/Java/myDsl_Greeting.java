





import java.util.List;
import java.util.ArrayList;

public class myDsl_Greeting  {

    private String question;





    private List<myDsl_Reponse> mydsl_reponses;




    private myDsl_Model mydsl_model;


    public myDsl_Greeting(
        String question    ) {
        this.question = question;
        this.mydsl_reponses = new ArrayList<>();
    }

    public myDsl_Greeting(
        String question        ArrayList<myDsl_Reponse> mydsl_reponses    ) {
        this.question = question;
        this.mydsl_reponses = mydsl_reponses;
    }

    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }

    public List<myDsl_Reponse> getMydsl_reponses() {
        return mydsl_reponses;
    }

    public void addMydsl_reponse(Mydsl_reponse mydsl_reponse) {
        this.mydsl_reponses.add(mydsl_reponse);
    }
    public myDsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(myDsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }

}