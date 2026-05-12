





import java.util.List;
import java.util.ArrayList;

public class spreadsheetGrammarLanguage_Grammar  {

    private String name;





    private spreadsheetGrammarLanguage_Block spreadsheetgrammarlanguage_block;


    public spreadsheetGrammarLanguage_Grammar(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public spreadsheetGrammarLanguage_Block getSpreadsheetgrammarlanguage_block() {
        return spreadsheetgrammarlanguage_block;
    }

    public void setSpreadsheetgrammarlanguage_block(spreadsheetGrammarLanguage_Block spreadsheetgrammarlanguage_block) {
        this.spreadsheetgrammarlanguage_block = spreadsheetgrammarlanguage_block;
    }

}