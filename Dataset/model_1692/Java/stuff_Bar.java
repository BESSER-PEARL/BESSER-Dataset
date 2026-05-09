





import java.util.List;
import java.util.ArrayList;

public class stuff_Bar extends NamedElement {






    private stuff_Stuff stuff_stuff;




    private List<stuff_Baz> stuff_bazs;


    public stuff_Bar(
    ) {
        super(
        );
        this.stuff_bazs = new ArrayList<>();
    }

    public stuff_Bar(
        ArrayList<stuff_Baz> stuff_bazs    ) {
        this.stuff_bazs = stuff_bazs;
    }


    public stuff_Stuff getStuff_stuff() {
        return stuff_stuff;
    }

    public void setStuff_stuff(stuff_Stuff stuff_stuff) {
        this.stuff_stuff = stuff_stuff;
    }
    public List<stuff_Baz> getStuff_bazs() {
        return stuff_bazs;
    }

    public void addStuff_baz(Stuff_baz stuff_baz) {
        this.stuff_bazs.add(stuff_baz);
    }

}