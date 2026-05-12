





import java.util.List;
import java.util.ArrayList;

public class ConsolePlayer  {

    private String name;
    private String score;



    public ConsolePlayer(
        String name,        String score    ) {
        this.name = name;
        this.score = score;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }


}