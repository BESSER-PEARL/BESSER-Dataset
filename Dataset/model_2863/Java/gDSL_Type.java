





import java.util.List;
import java.util.ArrayList;

public class gDSL_Type extends Decl {

    private String name;





    private List<gDSL_ConDecl> gdsl_condecls;


    public gDSL_Type(
        String name    ) {
        super(
        );
        this.name = name;
        this.gdsl_condecls = new ArrayList<>();
    }

    public gDSL_Type(
        String name        ArrayList<gDSL_ConDecl> gdsl_condecls    ) {
        this.name = name;
        this.gdsl_condecls = gdsl_condecls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gDSL_ConDecl> getGdsl_condecls() {
        return gdsl_condecls;
    }

    public void addGdsl_condecl(Gdsl_condecl gdsl_condecl) {
        this.gdsl_condecls.add(gdsl_condecl);
    }

}