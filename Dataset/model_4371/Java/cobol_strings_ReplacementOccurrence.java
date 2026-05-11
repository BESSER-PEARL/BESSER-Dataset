





import java.util.List;
import java.util.ArrayList;

public class cobol_strings_ReplacementOccurrence extends strings_Replacement, strings_Occurrence {






    private List<Replacement> replacements;


    public cobol_strings_ReplacementOccurrence(
    ) {
        super(
        );
        this.replacements = new ArrayList<>();
    }

    public cobol_strings_ReplacementOccurrence(
        ArrayList<Replacement> replacements    ) {
        this.replacements = replacements;
    }


    public List<Replacement> getReplacements() {
        return replacements;
    }

    public void addReplacement(Replacement replacement) {
        this.replacements.add(replacement);
    }

}