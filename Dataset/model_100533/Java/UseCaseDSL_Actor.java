





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_Actor  {

    private String type;
    private String name;
    private String description;





    private UseCaseDSL_Actor usecasedsl_actor;


    public UseCaseDSL_Actor(
        String type,        String name,        String description    ) {
        this.type = type;
        this.name = name;
        this.description = description;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
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

    public UseCaseDSL_Actor getUsecasedsl_actor() {
        return usecasedsl_actor;
    }

    public void setUsecasedsl_actor(UseCaseDSL_Actor usecasedsl_actor) {
        this.usecasedsl_actor = usecasedsl_actor;
    }

}