





import java.util.List;
import java.util.ArrayList;

public class ryz_UseCaseActorPackage extends Package {






    private List<ryz_Actor> ryz_actors;




    private List<ryz_UseCasePackage> ryz_usecasepackages;


    public ryz_UseCaseActorPackage(
    ) {
        super(
        );
        this.ryz_actors = new ArrayList<>();
        this.ryz_usecasepackages = new ArrayList<>();
    }

    public ryz_UseCaseActorPackage(
        ArrayList<ryz_Actor> ryz_actors,        ArrayList<ryz_UseCasePackage> ryz_usecasepackages    ) {
        this.ryz_actors = ryz_actors;
        this.ryz_usecasepackages = ryz_usecasepackages;
    }


    public List<ryz_Actor> getRyz_actors() {
        return ryz_actors;
    }

    public void addRyz_actor(Ryz_actor ryz_actor) {
        this.ryz_actors.add(ryz_actor);
    }
    public List<ryz_UseCasePackage> getRyz_usecasepackages() {
        return ryz_usecasepackages;
    }

    public void addRyz_usecasepackage(Ryz_usecasepackage ryz_usecasepackage) {
        this.ryz_usecasepackages.add(ryz_usecasepackage);
    }

}