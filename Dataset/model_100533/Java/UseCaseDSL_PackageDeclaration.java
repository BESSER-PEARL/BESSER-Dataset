





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_PackageDeclaration  {

    private String description;
    private String name;





    private List<UseCaseDSL_UseCase> usecasedsl_usecases;




    private List<UseCaseDSL_Actor> usecasedsl_actors;


    public UseCaseDSL_PackageDeclaration(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.usecasedsl_usecases = new ArrayList<>();
        this.usecasedsl_actors = new ArrayList<>();
    }

    public UseCaseDSL_PackageDeclaration(
        String description,        String name        ArrayList<UseCaseDSL_UseCase> usecasedsl_usecases,        ArrayList<UseCaseDSL_Actor> usecasedsl_actors    ) {
        this.description = description;
        this.name = name;
        this.usecasedsl_usecases = usecasedsl_usecases;
        this.usecasedsl_actors = usecasedsl_actors;
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

    public List<UseCaseDSL_UseCase> getUsecasedsl_usecases() {
        return usecasedsl_usecases;
    }

    public void addUsecasedsl_usecase(Usecasedsl_usecase usecasedsl_usecase) {
        this.usecasedsl_usecases.add(usecasedsl_usecase);
    }
    public List<UseCaseDSL_Actor> getUsecasedsl_actors() {
        return usecasedsl_actors;
    }

    public void addUsecasedsl_actor(Usecasedsl_actor usecasedsl_actor) {
        this.usecasedsl_actors.add(usecasedsl_actor);
    }

}