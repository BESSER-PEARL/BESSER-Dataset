





import java.util.List;
import java.util.ArrayList;

public class idl_FormalParameter  {

    private String name;





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

    public idl_TemplateModule getIdl_templatemodule() {
        return idl_templatemodule;
    }

    public void setIdl_templatemodule(idl_TemplateModule idl_templatemodule) {
        this.idl_templatemodule = idl_templatemodule;
    }

}