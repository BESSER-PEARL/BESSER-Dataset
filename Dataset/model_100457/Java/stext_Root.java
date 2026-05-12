





import java.util.List;
import java.util.ArrayList;

public class stext_Root  {






    private List<stext_DefRoot> stext_defroots;


    public stext_Root(
    ) {
        this.stext_defroots = new ArrayList<>();
    }

    public stext_Root(
        ArrayList<stext_DefRoot> stext_defroots    ) {
        this.stext_defroots = stext_defroots;
    }


    public List<stext_DefRoot> getStext_defroots() {
        return stext_defroots;
    }

    public void addStext_defroot(Stext_defroot stext_defroot) {
        this.stext_defroots.add(stext_defroot);
    }

}