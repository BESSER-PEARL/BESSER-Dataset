





import java.util.List;
import java.util.ArrayList;

public class cobol_strings_TallyingOccurrence extends strings_Tallying, strings_Occurrence {






    private List<Tallying> tallyings;


    public cobol_strings_TallyingOccurrence(
    ) {
        super(
        );
        this.tallyings = new ArrayList<>();
    }

    public cobol_strings_TallyingOccurrence(
        ArrayList<Tallying> tallyings    ) {
        this.tallyings = tallyings;
    }


    public List<Tallying> getTallyings() {
        return tallyings;
    }

    public void addTallying(Tallying tallying) {
        this.tallyings.add(tallying);
    }

}