





import java.util.List;
import java.util.ArrayList;

public class ryz_UseCase extends NamedElement {






    private List<ryz_ActionMethod> ryz_actionmethods;




    private ryz_ActionMethod ryz_actionmethod;




    private ryz_Actor ryz_actor;




    private ryz_UseCasePackage ryz_usecasepackage;




    private List<ryz_Actor> ryz_actors;


    public ryz_UseCase(
    ) {
        super(
        );
        this.ryz_actionmethods = new ArrayList<>();
        this.ryz_actors = new ArrayList<>();
    }

    public ryz_UseCase(
        ArrayList<ryz_ActionMethod> ryz_actionmethods,        ArrayList<ryz_Actor> ryz_actors    ) {
        this.ryz_actionmethods = ryz_actionmethods;
        this.ryz_actors = ryz_actors;
    }


    public List<ryz_ActionMethod> getRyz_actionmethods() {
        return ryz_actionmethods;
    }

    public void addRyz_actionmethod(Ryz_actionmethod ryz_actionmethod) {
        this.ryz_actionmethods.add(ryz_actionmethod);
    }
    public ryz_ActionMethod getRyz_actionmethod() {
        return ryz_actionmethod;
    }

    public void setRyz_actionmethod(ryz_ActionMethod ryz_actionmethod) {
        this.ryz_actionmethod = ryz_actionmethod;
    }
    public ryz_Actor getRyz_actor() {
        return ryz_actor;
    }

    public void setRyz_actor(ryz_Actor ryz_actor) {
        this.ryz_actor = ryz_actor;
    }
    public ryz_UseCasePackage getRyz_usecasepackage() {
        return ryz_usecasepackage;
    }

    public void setRyz_usecasepackage(ryz_UseCasePackage ryz_usecasepackage) {
        this.ryz_usecasepackage = ryz_usecasepackage;
    }
    public List<ryz_Actor> getRyz_actors() {
        return ryz_actors;
    }

    public void addRyz_actor(Ryz_actor ryz_actor) {
        this.ryz_actors.add(ryz_actor);
    }

}