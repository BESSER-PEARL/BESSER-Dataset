





import java.util.List;
import java.util.ArrayList;

public class alf_LocalNameDeclarationStatement extends Statement {






    private alf_MultiplicityIndicator alf_multiplicityindicator;




    private alf_TypeName alf_typename;




    private alf_Name alf_name;


    public alf_LocalNameDeclarationStatement(
    ) {
        super(
        );
    }



    public alf_MultiplicityIndicator getAlf_multiplicityindicator() {
        return alf_multiplicityindicator;
    }

    public void setAlf_multiplicityindicator(alf_MultiplicityIndicator alf_multiplicityindicator) {
        this.alf_multiplicityindicator = alf_multiplicityindicator;
    }
    public alf_TypeName getAlf_typename() {
        return alf_typename;
    }

    public void setAlf_typename(alf_TypeName alf_typename) {
        this.alf_typename = alf_typename;
    }
    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }

}