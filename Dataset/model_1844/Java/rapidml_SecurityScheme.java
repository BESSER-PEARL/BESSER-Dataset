





import java.util.List;
import java.util.ArrayList;

public class rapidml_SecurityScheme extends RESTElement, Documentable {

    private String name;
    private String flow;
    private String type;



    public rapidml_SecurityScheme(
        String name,        String flow,        String type    ) {
        super(
        );
        this.name = name;
        this.flow = flow;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFlow() {
        return flow;
    }

    public void setFlow(String flow) {
        this.flow = flow;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}