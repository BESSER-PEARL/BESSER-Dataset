





import java.util.List;
import java.util.ArrayList;

public class test_TestSuite extends NamedElement {

    private String description;
    private String api;



    public test_TestSuite(
        String description,        String api    ) {
        super(
        );
        this.description = description;
        this.api = api;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getApi() {
        return api;
    }

    public void setApi(String api) {
        this.api = api;
    }


}