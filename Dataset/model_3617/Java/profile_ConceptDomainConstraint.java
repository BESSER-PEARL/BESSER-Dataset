





import java.util.List;
import java.util.ArrayList;

public class profile_ConceptDomainConstraint  {

    private String name;
    private String identifier;



    public profile_ConceptDomainConstraint(
        String name,        String identifier    ) {
        this.name = name;
        this.identifier = identifier;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}