





import java.util.List;
import java.util.ArrayList;

public class typedef_Type  {

    private String name;





    private typedef_DocumentRoot typedef_documentroot;


    public typedef_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public typedef_DocumentRoot getTypedef_documentroot() {
        return typedef_documentroot;
    }

    public void setTypedef_documentroot(typedef_DocumentRoot typedef_documentroot) {
        this.typedef_documentroot = typedef_documentroot;
    }

}