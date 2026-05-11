





import java.util.List;
import java.util.ArrayList;

public class introduction_con  {






    private List<introduction_Y> introduction_ys;




    private List<introduction_A> introduction_as;


    public introduction_con(
    ) {
        this.introduction_ys = new ArrayList<>();
        this.introduction_as = new ArrayList<>();
    }

    public introduction_con(
        ArrayList<introduction_Y> introduction_ys,        ArrayList<introduction_A> introduction_as    ) {
        this.introduction_ys = introduction_ys;
        this.introduction_as = introduction_as;
    }


    public List<introduction_Y> getIntroduction_ys() {
        return introduction_ys;
    }

    public void addIntroduction_y(Introduction_y introduction_y) {
        this.introduction_ys.add(introduction_y);
    }
    public List<introduction_A> getIntroduction_as() {
        return introduction_as;
    }

    public void addIntroduction_a(Introduction_a introduction_a) {
        this.introduction_as.add(introduction_a);
    }

}