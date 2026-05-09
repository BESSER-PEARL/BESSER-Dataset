





import java.util.List;
import java.util.ArrayList;

public class myDsl_Module  {

    private String name;





    private List<myDsl_Submodule> mydsl_submodules;




    private myDsl_Domain mydsl_domain;


    public myDsl_Module(
        String name    ) {
        this.name = name;
        this.mydsl_submodules = new ArrayList<>();
    }

    public myDsl_Module(
        String name        ArrayList<myDsl_Submodule> mydsl_submodules    ) {
        this.name = name;
        this.mydsl_submodules = mydsl_submodules;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<myDsl_Submodule> getMydsl_submodules() {
        return mydsl_submodules;
    }

    public void addMydsl_submodule(Mydsl_submodule mydsl_submodule) {
        this.mydsl_submodules.add(mydsl_submodule);
    }
    public myDsl_Domain getMydsl_domain() {
        return mydsl_domain;
    }

    public void setMydsl_domain(myDsl_Domain mydsl_domain) {
        this.mydsl_domain = mydsl_domain;
    }

}