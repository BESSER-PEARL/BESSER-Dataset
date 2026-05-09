





import java.util.List;
import java.util.ArrayList;

public class model_UnicaseModelElement extends ModelElement {

    private String name;
    private String description;
    private String state;



    public model_UnicaseModelElement(
        String name,        String description,        String state    ) {
        super(
        );
        this.name = name;
        this.description = description;
        this.state = state;
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
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}