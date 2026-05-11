





import java.util.List;
import java.util.ArrayList;

public class SecCon_UseCase extends NamedElement {

    private String description;
    private String preCondition;





    private SecCon_UseCaseScenario seccon_usecasescenario;




    private List<SecCon_Actor> seccon_actors;




    private SecCon_UseCaseScenario seccon_usecasescenario;


    public SecCon_UseCase(
        String description,        String preCondition    ) {
        super(
        );
        this.description = description;
        this.preCondition = preCondition;
        this.seccon_actors = new ArrayList<>();
    }

    public SecCon_UseCase(
        String description,        String preCondition        ArrayList<SecCon_Actor> seccon_actors    ) {
        this.description = description;
        this.preCondition = preCondition;
        this.seccon_actors = seccon_actors;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPrecondition() {
        return preCondition;
    }

    public void setPrecondition(String preCondition) {
        this.preCondition = preCondition;
    }

    public SecCon_UseCaseScenario getSeccon_usecasescenario() {
        return seccon_usecasescenario;
    }

    public void setSeccon_usecasescenario(SecCon_UseCaseScenario seccon_usecasescenario) {
        this.seccon_usecasescenario = seccon_usecasescenario;
    }
    public List<SecCon_Actor> getSeccon_actors() {
        return seccon_actors;
    }

    public void addSeccon_actor(Seccon_actor seccon_actor) {
        this.seccon_actors.add(seccon_actor);
    }
    public SecCon_UseCaseScenario getSeccon_usecasescenario() {
        return seccon_usecasescenario;
    }

    public void setSeccon_usecasescenario(SecCon_UseCaseScenario seccon_usecasescenario) {
        this.seccon_usecasescenario = seccon_usecasescenario;
    }

}