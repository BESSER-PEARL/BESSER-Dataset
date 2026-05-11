





import java.util.List;
import java.util.ArrayList;

public class model_Query extends WSDLElement {

    private String queryLanguage;
    private String value;



    public model_Query(
        String queryLanguage,        String value    ) {
        super(
        );
        this.queryLanguage = queryLanguage;
        this.value = value;
    }


    public String getQuerylanguage() {
        return queryLanguage;
    }

    public void setQuerylanguage(String queryLanguage) {
        this.queryLanguage = queryLanguage;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}