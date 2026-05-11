





import java.util.List;
import java.util.ArrayList;

public class logoASM_Parameter  {

    private String name;





    private logoASM_ProcDeclaration logoasm_procdeclaration;


    public logoASM_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public logoASM_ProcDeclaration getLogoasm_procdeclaration() {
        return logoasm_procdeclaration;
    }

    public void setLogoasm_procdeclaration(logoASM_ProcDeclaration logoasm_procdeclaration) {
        this.logoasm_procdeclaration = logoasm_procdeclaration;
    }

}