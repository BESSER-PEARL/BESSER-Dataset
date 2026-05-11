





import java.util.List;
import java.util.ArrayList;

public class idl_IDLComment extends Definition, ConnectorExport, FixedDefinition, Export, PortExport, ComponentExport, TemplateDefinition {

    private String body;





    private idl_Module idl_module;


    public idl_IDLComment(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public idl_Module getIdl_module() {
        return idl_module;
    }

    public void setIdl_module(idl_Module idl_module) {
        this.idl_module = idl_module;
    }

}