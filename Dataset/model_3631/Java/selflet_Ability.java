





import java.util.List;
import java.util.ArrayList;

public class selflet_Ability  {

    private String file;
    private String service;





    private selflet_Abilities selflet_abilities;


    public selflet_Ability(
        String file,        String service    ) {
        this.file = file;
        this.service = service;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getService() {
        return service;
    }

    public void setService(String service) {
        this.service = service;
    }

    public selflet_Abilities getSelflet_abilities() {
        return selflet_abilities;
    }

    public void setSelflet_abilities(selflet_Abilities selflet_abilities) {
        this.selflet_abilities = selflet_abilities;
    }

}