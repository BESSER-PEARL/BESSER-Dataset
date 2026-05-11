





import java.util.List;
import java.util.ArrayList;

public class idl_Module extends Definition {

    private String name;





    private List<idl_Definition> idl_definitions;


    public idl_Module(
        String name    ) {
        super(
        );
        this.name = name;
        this.idl_definitions = new ArrayList<>();
    }

    public idl_Module(
        String name        ArrayList<idl_Definition> idl_definitions    ) {
        this.name = name;
        this.idl_definitions = idl_definitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<idl_Definition> getIdl_definitions() {
        return idl_definitions;
    }

    public void addIdl_definition(Idl_definition idl_definition) {
        this.idl_definitions.add(idl_definition);
    }

}