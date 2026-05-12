





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_richstring_RichStringOrderedList extends RichStringMarkup {






    private List<RichStringListElement> richstringlistelements;


    public luniferadoc_richstring_RichStringOrderedList(
    ) {
        super(
        );
        this.richstringlistelements = new ArrayList<>();
    }

    public luniferadoc_richstring_RichStringOrderedList(
        ArrayList<RichStringListElement> richstringlistelements    ) {
        this.richstringlistelements = richstringlistelements;
    }


    public List<RichStringListElement> getRichstringlistelements() {
        return richstringlistelements;
    }

    public void addRichstringlistelement(Richstringlistelement richstringlistelement) {
        this.richstringlistelements.add(richstringlistelement);
    }

}