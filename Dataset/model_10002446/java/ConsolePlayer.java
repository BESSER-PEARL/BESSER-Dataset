





import java.util.List;
import java.util.ArrayList;

public class ConsolePlayer  {

    private String score;
    private String name;



    public ConsolePlayer(
        String score,        String name    ) {
        this.score = score;
        this.name = name;
    }


    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}