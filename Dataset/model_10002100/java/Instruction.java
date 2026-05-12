





import java.util.List;
import java.util.ArrayList;

public class Instruction  {

    private String title;
    private int level;



    public Instruction(
        String title,        int level    ) {
        this.title = title;
        this.level = level;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }


}