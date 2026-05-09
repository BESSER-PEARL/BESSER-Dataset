





import java.util.List;
import java.util.ArrayList;

public class bibtexml_BibTeXMLEntryType extends BibTeXMLEntriesClass {

    private String id;



    public bibtexml_BibTeXMLEntryType(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}