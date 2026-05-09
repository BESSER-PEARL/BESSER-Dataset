





import java.util.List;
import java.util.ArrayList;

public class esmodel_accesscontrol_ACOrgUnit extends IdentifiableElement {

    private String name;
    private String description;



    public esmodel_accesscontrol_ACOrgUnit(
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