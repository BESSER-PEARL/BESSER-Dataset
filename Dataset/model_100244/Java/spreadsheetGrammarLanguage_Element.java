





import java.util.List;
import java.util.ArrayList;

public class spreadsheetGrammarLanguage_Element  {

    private String name;





    private spreadsheetGrammarLanguage_Grammar spreadsheetgrammarlanguage_grammar;


    public spreadsheetGrammarLanguage_Element(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public spreadsheetGrammarLanguage_Grammar getSpreadsheetgrammarlanguage_grammar() {
        return spreadsheetgrammarlanguage_grammar;
    }

    public void setSpreadsheetgrammarlanguage_grammar(spreadsheetGrammarLanguage_Grammar spreadsheetgrammarlanguage_grammar) {
        this.spreadsheetgrammarlanguage_grammar = spreadsheetgrammarlanguage_grammar;
    }

}