





import java.util.List;
import java.util.ArrayList;

public class service_syntax_InterfaceDescription  {

    private String name;





    private List<syntax_service_SchemaType> syntax_service_schematypes;




    private syntax_service_SchemaType syntax_service_schematype;


    public service_syntax_InterfaceDescription(
        String name    ) {
        this.name = name;
        this.syntax_service_schematypes = new ArrayList<>();
    }

    public service_syntax_InterfaceDescription(
        String name        ArrayList<syntax_service_SchemaType> syntax_service_schematypes    ) {
        this.name = name;
        this.syntax_service_schematypes = syntax_service_schematypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<syntax_service_SchemaType> getSyntax_service_schematypes() {
        return syntax_service_schematypes;
    }

    public void addSyntax_service_schematype(Syntax_service_schematype syntax_service_schematype) {
        this.syntax_service_schematypes.add(syntax_service_schematype);
    }
    public syntax_service_SchemaType getSyntax_service_schematype() {
        return syntax_service_schematype;
    }

    public void setSyntax_service_schematype(syntax_service_SchemaType syntax_service_schematype) {
        this.syntax_service_schematype = syntax_service_schematype;
    }

}