





import java.util.List;
import java.util.ArrayList;

public class go_SignatureDel  {

    private String id;





    private go_Types go_types;




    private go_VarDecl go_vardecl;




    private go_TIPO go_tipo;


    public go_SignatureDel(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public go_Types getGo_types() {
        return go_types;
    }

    public void setGo_types(go_Types go_types) {
        this.go_types = go_types;
    }
    public go_VarDecl getGo_vardecl() {
        return go_vardecl;
    }

    public void setGo_vardecl(go_VarDecl go_vardecl) {
        this.go_vardecl = go_vardecl;
    }
    public go_TIPO getGo_tipo() {
        return go_tipo;
    }

    public void setGo_tipo(go_TIPO go_tipo) {
        this.go_tipo = go_tipo;
    }

}