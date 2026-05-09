





import java.util.List;
import java.util.ArrayList;

public class occi_Constraint  {

    private String body;
    private String name;
    private String description;



    public occi_Constraint(
        String body,        String name,        String description    ) {
        this.body = body;
        this.name = name;
        this.description = description;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}