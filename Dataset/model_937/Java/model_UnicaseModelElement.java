





import java.util.List;
import java.util.ArrayList;

public class model_UnicaseModelElement extends ModelElement {

    private String description;
    private String name;
    private String state;



    public model_UnicaseModelElement(
        String description,        String name,        String state    ) {
        super(
        );
        this.description = description;
        this.name = name;
        this.state = state;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
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


}