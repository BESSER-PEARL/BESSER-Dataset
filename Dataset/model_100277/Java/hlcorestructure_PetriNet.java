





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_PetriNet  {

    private String type;
    private String id;





    private hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc;




    private hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc;




    private hlcorestructure_Declaration hlcorestructure_declaration;




    private List<hlcorestructure_Declaration> hlcorestructure_declarations;


    public hlcorestructure_PetriNet(
        String type,        String id    ) {
        this.type = type;
        this.id = id;
        this.hlcorestructure_declarations = new ArrayList<>();
    }

    public hlcorestructure_PetriNet(
        String type,        String id        ArrayList<hlcorestructure_Declaration> hlcorestructure_declarations    ) {
        this.type = type;
        this.id = id;
        this.hlcorestructure_declarations = hlcorestructure_declarations;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public hlcorestructure_PetriNetDoc getHlcorestructure_petrinetdoc() {
        return hlcorestructure_petrinetdoc;
    }

    public void setHlcorestructure_petrinetdoc(hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc) {
        this.hlcorestructure_petrinetdoc = hlcorestructure_petrinetdoc;
    }
    public hlcorestructure_PetriNetDoc getHlcorestructure_petrinetdoc() {
        return hlcorestructure_petrinetdoc;
    }

    public void setHlcorestructure_petrinetdoc(hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc) {
        this.hlcorestructure_petrinetdoc = hlcorestructure_petrinetdoc;
    }
    public hlcorestructure_Declaration getHlcorestructure_declaration() {
        return hlcorestructure_declaration;
    }

    public void setHlcorestructure_declaration(hlcorestructure_Declaration hlcorestructure_declaration) {
        this.hlcorestructure_declaration = hlcorestructure_declaration;
    }
    public List<hlcorestructure_Declaration> getHlcorestructure_declarations() {
        return hlcorestructure_declarations;
    }

    public void addHlcorestructure_declaration(Hlcorestructure_declaration hlcorestructure_declaration) {
        this.hlcorestructure_declarations.add(hlcorestructure_declaration);
    }

}