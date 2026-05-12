





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_Page extends PnObject {






    private hlcorestructure_PetriNet hlcorestructure_petrinet;




    private List<hlcorestructure_Declaration> hlcorestructure_declarations;




    private hlcorestructure_PetriNet hlcorestructure_petrinet;




    private hlcorestructure_Declaration hlcorestructure_declaration;


    public hlcorestructure_Page(
    ) {
        super(
        );
        this.hlcorestructure_declarations = new ArrayList<>();
    }

    public hlcorestructure_Page(
        ArrayList<hlcorestructure_Declaration> hlcorestructure_declarations    ) {
        this.hlcorestructure_declarations = hlcorestructure_declarations;
    }


    public hlcorestructure_PetriNet getHlcorestructure_petrinet() {
        return hlcorestructure_petrinet;
    }

    public void setHlcorestructure_petrinet(hlcorestructure_PetriNet hlcorestructure_petrinet) {
        this.hlcorestructure_petrinet = hlcorestructure_petrinet;
    }
    public List<hlcorestructure_Declaration> getHlcorestructure_declarations() {
        return hlcorestructure_declarations;
    }

    public void addHlcorestructure_declaration(Hlcorestructure_declaration hlcorestructure_declaration) {
        this.hlcorestructure_declarations.add(hlcorestructure_declaration);
    }
    public hlcorestructure_PetriNet getHlcorestructure_petrinet() {
        return hlcorestructure_petrinet;
    }

    public void setHlcorestructure_petrinet(hlcorestructure_PetriNet hlcorestructure_petrinet) {
        this.hlcorestructure_petrinet = hlcorestructure_petrinet;
    }
    public hlcorestructure_Declaration getHlcorestructure_declaration() {
        return hlcorestructure_declaration;
    }

    public void setHlcorestructure_declaration(hlcorestructure_Declaration hlcorestructure_declaration) {
        this.hlcorestructure_declaration = hlcorestructure_declaration;
    }

}