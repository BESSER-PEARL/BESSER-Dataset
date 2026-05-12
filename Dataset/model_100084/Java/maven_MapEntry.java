





import java.util.List;
import java.util.ArrayList;

public class maven_MapEntry extends GroupAndArtifact {

    private String name;





    private List<maven_GroupAndArtifact> maven_groupandartifacts;


    public maven_MapEntry(
        String name    ) {
        super(
        );
        this.name = name;
        this.maven_groupandartifacts = new ArrayList<>();
    }

    public maven_MapEntry(
        String name        ArrayList<maven_GroupAndArtifact> maven_groupandartifacts    ) {
        this.name = name;
        this.maven_groupandartifacts = maven_groupandartifacts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<maven_GroupAndArtifact> getMaven_groupandartifacts() {
        return maven_groupandartifacts;
    }

    public void addMaven_groupandartifact(Maven_groupandartifact maven_groupandartifact) {
        this.maven_groupandartifacts.add(maven_groupandartifact);
    }

}