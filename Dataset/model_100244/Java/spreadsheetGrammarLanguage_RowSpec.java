





import java.util.List;
import java.util.ArrayList;

public class spreadsheetGrammarLanguage_RowSpec extends ColumnSpec {

    private String header;



    public spreadsheetGrammarLanguage_RowSpec(
        String header    ) {
        super(
        );
        this.header = header;
    }


    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }


}