





import java.util.List;
import java.util.ArrayList;

public class article_Toc extends BodyElement {

    private int levels;



    public article_Toc(
        int levels    ) {
        super(
        );
        this.levels = levels;
    }


    public int getLevels() {
        return levels;
    }

    public void setLevels(int levels) {
        this.levels = levels;
    }


}