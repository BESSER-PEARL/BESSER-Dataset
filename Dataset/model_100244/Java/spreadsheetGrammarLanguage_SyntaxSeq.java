





import java.util.List;
import java.util.ArrayList;

public class spreadsheetGrammarLanguage_SyntaxSeq  {






    private List<spreadsheetGrammarLanguage_Syntax> spreadsheetgrammarlanguage_syntaxs;




    private spreadsheetGrammarLanguage_Rule spreadsheetgrammarlanguage_rule;


    public spreadsheetGrammarLanguage_SyntaxSeq(
    ) {
        this.spreadsheetgrammarlanguage_syntaxs = new ArrayList<>();
    }

    public spreadsheetGrammarLanguage_SyntaxSeq(
        ArrayList<spreadsheetGrammarLanguage_Syntax> spreadsheetgrammarlanguage_syntaxs    ) {
        this.spreadsheetgrammarlanguage_syntaxs = spreadsheetgrammarlanguage_syntaxs;
    }


    public List<spreadsheetGrammarLanguage_Syntax> getSpreadsheetgrammarlanguage_syntaxs() {
        return spreadsheetgrammarlanguage_syntaxs;
    }

    public void addSpreadsheetgrammarlanguage_syntax(Spreadsheetgrammarlanguage_syntax spreadsheetgrammarlanguage_syntax) {
        this.spreadsheetgrammarlanguage_syntaxs.add(spreadsheetgrammarlanguage_syntax);
    }
    public spreadsheetGrammarLanguage_Rule getSpreadsheetgrammarlanguage_rule() {
        return spreadsheetgrammarlanguage_rule;
    }

    public void setSpreadsheetgrammarlanguage_rule(spreadsheetGrammarLanguage_Rule spreadsheetgrammarlanguage_rule) {
        this.spreadsheetgrammarlanguage_rule = spreadsheetgrammarlanguage_rule;
    }

}