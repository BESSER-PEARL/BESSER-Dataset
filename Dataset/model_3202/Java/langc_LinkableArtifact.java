





import java.util.List;
import java.util.ArrayList;

public class langc_LinkableArtifact  {

    private String name;





    private langc_System langc_system;




    private List<langc_UserElement> langc_userelements;




    private List<langc_FunctionImplementation> langc_functionimplementations;


    public langc_LinkableArtifact(
        String name    ) {
        this.name = name;
        this.langc_userelements = new ArrayList<>();
        this.langc_functionimplementations = new ArrayList<>();
    }

    public langc_LinkableArtifact(
        String name        ArrayList<langc_UserElement> langc_userelements,        ArrayList<langc_FunctionImplementation> langc_functionimplementations    ) {
        this.name = name;
        this.langc_userelements = langc_userelements;
        this.langc_functionimplementations = langc_functionimplementations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public langc_System getLangc_system() {
        return langc_system;
    }

    public void setLangc_system(langc_System langc_system) {
        this.langc_system = langc_system;
    }
    public List<langc_UserElement> getLangc_userelements() {
        return langc_userelements;
    }

    public void addLangc_userelement(Langc_userelement langc_userelement) {
        this.langc_userelements.add(langc_userelement);
    }
    public List<langc_FunctionImplementation> getLangc_functionimplementations() {
        return langc_functionimplementations;
    }

    public void addLangc_functionimplementation(Langc_functionimplementation langc_functionimplementation) {
        this.langc_functionimplementations.add(langc_functionimplementation);
    }

}