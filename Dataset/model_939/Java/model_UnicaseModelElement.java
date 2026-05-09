





import java.util.List;
import java.util.ArrayList;

public class model_UnicaseModelElement extends ModelElement {

    private String name;
    private String state;
    private String description;



    public model_UnicaseModelElement(
        String name,        String state,        String description    ) {
        super(
        );
        this.name = name;
        this.state = state;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}