





import java.util.List;
import java.util.ArrayList;

public class website_EnumerationType extends DataType {






    private List<website_EnumerationLiteral> website_enumerationliterals;


    public website_EnumerationType(
    ) {
        super(
        );
        this.website_enumerationliterals = new ArrayList<>();
    }

    public website_EnumerationType(
        ArrayList<website_EnumerationLiteral> website_enumerationliterals    ) {
        this.website_enumerationliterals = website_enumerationliterals;
    }


    public List<website_EnumerationLiteral> getWebsite_enumerationliterals() {
        return website_enumerationliterals;
    }

    public void addWebsite_enumerationliteral(Website_enumerationliteral website_enumerationliteral) {
        this.website_enumerationliterals.add(website_enumerationliteral);
    }

}