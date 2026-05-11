





import java.util.List;
import java.util.ArrayList;

public class alf_LocalNameDeclarationStatement extends Statement {

    private boolean multiplicityIndicator;
    private String varName;





    private alf_QualifiedNameWithBinding alf_qualifiednamewithbinding;


    public alf_LocalNameDeclarationStatement(
        boolean multiplicityIndicator,        String varName    ) {
        super(
        );
        this.multiplicityIndicator = multiplicityIndicator;
        this.varName = varName;
    }


    public boolean getMultiplicityindicator() {
        return multiplicityIndicator;
    }

    public void setMultiplicityindicator(boolean multiplicityIndicator) {
        this.multiplicityIndicator = multiplicityIndicator;
    }
    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public alf_QualifiedNameWithBinding getAlf_qualifiednamewithbinding() {
        return alf_qualifiednamewithbinding;
    }

    public void setAlf_qualifiednamewithbinding(alf_QualifiedNameWithBinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbinding = alf_qualifiednamewithbinding;
    }

}