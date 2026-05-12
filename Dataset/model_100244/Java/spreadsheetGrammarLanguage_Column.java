





import java.util.List;
import java.util.ArrayList;

public class spreadsheetGrammarLanguage_Column  {

    private boolean multiple;
    private String name;





    private spreadsheetGrammarLanguage_Block spreadsheetgrammarlanguage_block;


    public spreadsheetGrammarLanguage_Column(
        boolean multiple,        String name    ) {
        this.multiple = multiple;
        this.name = name;
    }


    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
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