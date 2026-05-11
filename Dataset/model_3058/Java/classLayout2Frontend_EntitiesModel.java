





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_EntitiesModel  {

    private String name;





    private List<classLayout2Frontend_EntityModelElement> classlayout2frontend_entitymodelelements;




    private classLayout2Frontend_Project classlayout2frontend_project;


    public classLayout2Frontend_EntitiesModel(
        String name    ) {
        this.name = name;
        this.classlayout2frontend_entitymodelelements = new ArrayList<>();
    }

    public classLayout2Frontend_EntitiesModel(
        String name        ArrayList<classLayout2Frontend_EntityModelElement> classlayout2frontend_entitymodelelements    ) {
        this.name = name;
        this.classlayout2frontend_entitymodelelements = classlayout2frontend_entitymodelelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<classLayout2Frontend_EntityModelElement> getClasslayout2frontend_entitymodelelements() {
        return classlayout2frontend_entitymodelelements;
    }

    public void addClasslayout2frontend_entitymodelelement(Classlayout2frontend_entitymodelelement classlayout2frontend_entitymodelelement) {
        this.classlayout2frontend_entitymodelelements.add(classlayout2frontend_entitymodelelement);
    }
    public classLayout2Frontend_Project getClasslayout2frontend_project() {
        return classlayout2frontend_project;
    }

    public void setClasslayout2frontend_project(classLayout2Frontend_Project classlayout2frontend_project) {
        this.classlayout2frontend_project = classlayout2frontend_project;
    }

}