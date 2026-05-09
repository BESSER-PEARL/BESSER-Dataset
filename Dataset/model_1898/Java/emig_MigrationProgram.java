





import java.util.List;
import java.util.ArrayList;

public class emig_MigrationProgram extends LocatedElement {

    private String delta;
    private String migr;
    private String libs;
    private String name;
    private String artifact;





    private emig_MyModel emig_mymodel;


    public emig_MigrationProgram(
        String delta,        String migr,        String libs,        String name,        String artifact    ) {
        super(
        );
        this.delta = delta;
        this.migr = migr;
        this.libs = libs;
        this.name = name;
        this.artifact = artifact;
    }


    public String getDelta() {
        return delta;
    }

    public void setDelta(String delta) {
        this.delta = delta;
    }
    public String getMigr() {
        return migr;
    }

    public void setMigr(String migr) {
        this.migr = migr;
    }
    public String getLibs() {
        return libs;
    }

    public void setLibs(String libs) {
        this.libs = libs;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getArtifact() {
        return artifact;
    }

    public void setArtifact(String artifact) {
        this.artifact = artifact;
    }

    public emig_MyModel getEmig_mymodel() {
        return emig_mymodel;
    }

    public void setEmig_mymodel(emig_MyModel emig_mymodel) {
        this.emig_mymodel = emig_mymodel;
    }

}