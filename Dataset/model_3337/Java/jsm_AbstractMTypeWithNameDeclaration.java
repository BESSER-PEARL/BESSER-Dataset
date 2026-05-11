





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractMTypeWithNameDeclaration  {

    private String name;





    private jsm_AbstractMTypeReference jsm_abstractmtypereference;


    public jsm_AbstractMTypeWithNameDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jsm_AbstractMTypeReference getJsm_abstractmtypereference() {
        return jsm_abstractmtypereference;
    }

    public void setJsm_abstractmtypereference(jsm_AbstractMTypeReference jsm_abstractmtypereference) {
        this.jsm_abstractmtypereference = jsm_abstractmtypereference;
    }

}