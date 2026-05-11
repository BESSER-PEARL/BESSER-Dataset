





import java.util.List;
import java.util.ArrayList;

public class alf_LocalNameDeclarationStatement extends Statement {

    private boolean multiplicityIndicator;
    private String varName;





    private alf_SequenceElement alf_sequenceelement;


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

    public alf_SequenceElement getAlf_sequenceelement() {
        return alf_sequenceelement;
    }

    public void setAlf_sequenceelement(alf_SequenceElement alf_sequenceelement) {
        this.alf_sequenceelement = alf_sequenceelement;
    }

}