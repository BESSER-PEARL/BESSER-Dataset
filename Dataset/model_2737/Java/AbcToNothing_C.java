





import java.util.List;
import java.util.ArrayList;

public class AbcToNothing_C  {






    private AbcToNothing_A abctonothing_a;




    private List<AbcToNothing_classB> abctonothing_classbs;


    public AbcToNothing_C(
    ) {
        this.abctonothing_classbs = new ArrayList<>();
    }

    public AbcToNothing_C(
        ArrayList<AbcToNothing_classB> abctonothing_classbs    ) {
        this.abctonothing_classbs = abctonothing_classbs;
    }


    public AbcToNothing_A getAbctonothing_a() {
        return abctonothing_a;
    }

    public void setAbctonothing_a(AbcToNothing_A abctonothing_a) {
        this.abctonothing_a = abctonothing_a;
    }
    public List<AbcToNothing_classB> getAbctonothing_classbs() {
        return abctonothing_classbs;
    }

    public void addAbctonothing_classb(Abctonothing_classb abctonothing_classb) {
        this.abctonothing_classbs.add(abctonothing_classb);
    }

}