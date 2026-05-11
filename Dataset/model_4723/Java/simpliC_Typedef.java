





import java.util.List;
import java.util.ArrayList;

public class simpliC_Typedef extends Stmt {

    private String name;





    private simpliC_Decl simplic_decl;


    public simpliC_Typedef(
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

    public simpliC_Decl getSimplic_decl() {
        return simplic_decl;
    }

    public void setSimplic_decl(simpliC_Decl simplic_decl) {
        this.simplic_decl = simplic_decl;
    }

}