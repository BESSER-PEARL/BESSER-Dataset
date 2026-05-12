





import java.util.List;
import java.util.ArrayList;

public class spreadsheetGrammarLanguage_Syntax  {

    private boolean is_int;
    private boolean is_string;
    private String token;
    private boolean is_id;





    private spreadsheetGrammarLanguage_RowSpec spreadsheetgrammarlanguage_rowspec;




    private spreadsheetGrammarLanguage_Rule spreadsheetgrammarlanguage_rule;


    public spreadsheetGrammarLanguage_Syntax(
        boolean is_int,        boolean is_string,        String token,        boolean is_id    ) {
        this.is_int = is_int;
        this.is_string = is_string;
        this.token = token;
        this.is_id = is_id;
    }


    public boolean getIs_int() {
        return is_int;
    }

    public void setIs_int(boolean is_int) {
        this.is_int = is_int;
    }
    public boolean getIs_string() {
        return is_string;
    }

    public void setIs_string(boolean is_string) {
        this.is_string = is_string;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
    public boolean getIs_id() {
        return is_id;
    }

    public void setIs_id(boolean is_id) {
        this.is_id = is_id;
    }

    public spreadsheetGrammarLanguage_RowSpec getSpreadsheetgrammarlanguage_rowspec() {
        return spreadsheetgrammarlanguage_rowspec;
    }

    public void setSpreadsheetgrammarlanguage_rowspec(spreadsheetGrammarLanguage_RowSpec spreadsheetgrammarlanguage_rowspec) {
        this.spreadsheetgrammarlanguage_rowspec = spreadsheetgrammarlanguage_rowspec;
    }
    public spreadsheetGrammarLanguage_Rule getSpreadsheetgrammarlanguage_rule() {
        return spreadsheetgrammarlanguage_rule;
    }

    public void setSpreadsheetgrammarlanguage_rule(spreadsheetGrammarLanguage_Rule spreadsheetgrammarlanguage_rule) {
        this.spreadsheetgrammarlanguage_rule = spreadsheetgrammarlanguage_rule;
    }

}