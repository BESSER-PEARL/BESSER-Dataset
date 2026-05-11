





import java.util.List;
import java.util.ArrayList;

public class idl_TemplateModule extends Definition {

    private String name;





    private List<idl_TemplateDefinition> idl_templatedefinitions;


    public idl_TemplateModule(
        String name    ) {
        super(
        );
        this.name = name;
        this.idl_templatedefinitions = new ArrayList<>();
    }

    public idl_TemplateModule(
        String name        ArrayList<idl_TemplateDefinition> idl_templatedefinitions    ) {
        this.name = name;
        this.idl_templatedefinitions = idl_templatedefinitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<idl_TemplateDefinition> getIdl_templatedefinitions() {
        return idl_templatedefinitions;
    }

    public void addIdl_templatedefinition(Idl_templatedefinition idl_templatedefinition) {
        this.idl_templatedefinitions.add(idl_templatedefinition);
    }

}