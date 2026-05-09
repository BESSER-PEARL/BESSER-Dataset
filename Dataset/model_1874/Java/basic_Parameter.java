





import java.util.List;
import java.util.ArrayList;

public class basic_Parameter  {

    private String name;
    private String description;
    private String type;





    private basic_Event basic_event;


    public basic_Parameter(
        String name,        String description,        String type    ) {
        this.name = name;
        this.description = description;
        this.type = type;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public basic_Event getBasic_event() {
        return basic_event;
    }

    public void setBasic_event(basic_Event basic_event) {
        this.basic_event = basic_event;
    }

}