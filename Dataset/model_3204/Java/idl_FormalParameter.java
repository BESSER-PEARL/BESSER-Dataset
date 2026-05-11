





import java.util.List;
import java.util.ArrayList;

public class idl_FormalParameter  {

    private String name;





    private idl_FormalParameterType idl_formalparametertype;




    private idl_TemplateModule idl_templatemodule;


    public idl_FormalParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public idl_FormalParameterType getIdl_formalparametertype() {
        return idl_formalparametertype;
    }

    public void setIdl_formalparametertype(idl_FormalParameterType idl_formalparametertype) {
        this.idl_formalparametertype = idl_formalparametertype;
    }
    public idl_TemplateModule getIdl_templatemodule() {
        return idl_templatemodule;
    }

    public void setIdl_templatemodule(idl_TemplateModule idl_templatemodule) {
        this.idl_templatemodule = idl_templatemodule;
    }

}