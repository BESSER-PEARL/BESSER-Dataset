





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_Actor  {

    private String description;
    private String name;
    private String type;





    private UseCaseDSL_Actor usecasedsl_actor;


    public UseCaseDSL_Actor(
        String description,        String name,        String type    ) {
        this.description = description;
        this.name = name;
        this.type = type;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public UseCaseDSL_Actor getUsecasedsl_actor() {
        return usecasedsl_actor;
    }

    public void setUsecasedsl_actor(UseCaseDSL_Actor usecasedsl_actor) {
        this.usecasedsl_actor = usecasedsl_actor;
    }

}