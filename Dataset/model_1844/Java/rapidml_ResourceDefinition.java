





import java.util.List;
import java.util.ArrayList;

public class rapidml_ResourceDefinition extends WithExamples, RESTElement, HasSecurityValue {

    private String name;



    public rapidml_ResourceDefinition(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}