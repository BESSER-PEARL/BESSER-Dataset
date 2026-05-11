





import java.util.List;
import java.util.ArrayList;

public class ale_Unit  {

    private String name;





    private List<ale_Import> ale_imports;




    private List<ale_Service> ale_services;




    private List<ale_BehavioredClass> ale_behavioredclasss;


    public ale_Unit(
        String name    ) {
        this.name = name;
        this.ale_imports = new ArrayList<>();
        this.ale_services = new ArrayList<>();
        this.ale_behavioredclasss = new ArrayList<>();
    }

    public ale_Unit(
        String name        ArrayList<ale_Import> ale_imports,        ArrayList<ale_Service> ale_services,        ArrayList<ale_BehavioredClass> ale_behavioredclasss    ) {
        this.name = name;
        this.ale_imports = ale_imports;
        this.ale_services = ale_services;
        this.ale_behavioredclasss = ale_behavioredclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ale_Import> getAle_imports() {
        return ale_imports;
    }

    public void addAle_import(Ale_import ale_import) {
        this.ale_imports.add(ale_import);
    }
    public List<ale_Service> getAle_services() {
        return ale_services;
    }

    public void addAle_service(Ale_service ale_service) {
        this.ale_services.add(ale_service);
    }
    public List<ale_BehavioredClass> getAle_behavioredclasss() {
        return ale_behavioredclasss;
    }

    public void addAle_behavioredclass(Ale_behavioredclass ale_behavioredclass) {
        this.ale_behavioredclasss.add(ale_behavioredclass);
    }

}