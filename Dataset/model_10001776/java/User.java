





import java.util.List;
import java.util.ArrayList;

public class User  {






    private List<QuestonOrAnswer> questonoranswers;


    public User(
    ) {
        this.questonoranswers = new ArrayList<>();
    }

    public User(
        ArrayList<QuestonOrAnswer> questonoranswers    ) {
        this.questonoranswers = questonoranswers;
    }


    public List<QuestonOrAnswer> getQuestonoranswers() {
        return questonoranswers;
    }

    public void addQuestonoranswer(Questonoranswer questonoranswer) {
        this.questonoranswers.add(questonoranswer);
    }

}