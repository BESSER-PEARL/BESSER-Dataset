





import java.util.List;
import java.util.ArrayList;

public class emig_MigrationProgram  {

    private String delta;
    private String libs;
    private String migr;
    private String name;





    private emig_MyModel emig_mymodel;


    public emig_MigrationProgram(
        String delta,        String libs,        String migr,        String name    ) {
        this.delta = delta;
        this.libs = libs;
        this.migr = migr;
        this.name = name;
    }


    public String getDelta() {
        return delta;
    }

    public void setDelta(String delta) {
        this.delta = delta;
    }
    public String getLibs() {
        return libs;
    }

    public void setLibs(String libs) {
        this.libs = libs;
    }
    public String getMigr() {
        return migr;
    }

    public void setMigr(String migr) {
        this.migr = migr;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emig_MyModel getEmig_mymodel() {
        return emig_mymodel;
    }

    public void setEmig_mymodel(emig_MyModel emig_mymodel) {
        this.emig_mymodel = emig_mymodel;
    }

}