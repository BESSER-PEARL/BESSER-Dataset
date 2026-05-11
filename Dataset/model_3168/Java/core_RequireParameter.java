





import java.util.List;
import java.util.ArrayList;

public class core_RequireParameter  {

    private String formalParameterName;





    private core_RequireDeclaration core_requiredeclaration;


    public core_RequireParameter(
        String formalParameterName    ) {
        this.formalParameterName = formalParameterName;
    }


    public String getFormalparametername() {
        return formalParameterName;
    }

    public void setFormalparametername(String formalParameterName) {
        this.formalParameterName = formalParameterName;
    }

    public core_RequireDeclaration getCore_requiredeclaration() {
        return core_requiredeclaration;
    }

    public void setCore_requiredeclaration(core_RequireDeclaration core_requiredeclaration) {
        this.core_requiredeclaration = core_requiredeclaration;
    }

}