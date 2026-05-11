





import java.util.List;
import java.util.ArrayList;

public class idl_ConstDecl extends TemplateDefinition, Export, Definition, FixedDefinition {

    private String name;





    private idl_ConstExp idl_constexp;


    public idl_ConstDecl(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public idl_ConstExp getIdl_constexp() {
        return idl_constexp;
    }

    public void setIdl_constexp(idl_ConstExp idl_constexp) {
        this.idl_constexp = idl_constexp;
    }

}