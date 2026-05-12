





import java.util.List;
import java.util.ArrayList;

public class useCases_Actor  {

    private String description;
    private String name;
    private String type;





    private useCases_Actor usecases_actor;




    private useCases_PackageDeclaration usecases_packagedeclaration;


    public useCases_Actor(
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

    public useCases_Actor getUsecases_actor() {
        return usecases_actor;
    }

    public void setUsecases_actor(useCases_Actor usecases_actor) {
        this.usecases_actor = usecases_actor;
    }
    public useCases_PackageDeclaration getUsecases_packagedeclaration() {
        return usecases_packagedeclaration;
    }

    public void setUsecases_packagedeclaration(useCases_PackageDeclaration usecases_packagedeclaration) {
        this.usecases_packagedeclaration = usecases_packagedeclaration;
    }

}