





import java.util.List;
import java.util.ArrayList;

public class henshin_NamedElement extends ModelElement {

    private String name;
    private String description;



    public henshin_NamedElement(
        String name,        String description    ) {
        super(
        );
        this.name = name;
        this.description = description;
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