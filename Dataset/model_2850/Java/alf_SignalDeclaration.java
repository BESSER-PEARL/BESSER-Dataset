





import java.util.List;
import java.util.ArrayList;

public class alf_SignalDeclaration  {

    private boolean isAbstract;





    private alf_SignalDefinition alf_signaldefinition;




    private alf_SignalDefinitionOrStub alf_signaldefinitionorstub;




    private alf_ClassifierSignature alf_classifiersignature;


    public alf_SignalDeclaration(
        boolean isAbstract    ) {
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public alf_SignalDefinition getAlf_signaldefinition() {
        return alf_signaldefinition;
    }

    public void setAlf_signaldefinition(alf_SignalDefinition alf_signaldefinition) {
        this.alf_signaldefinition = alf_signaldefinition;
    }
    public alf_SignalDefinitionOrStub getAlf_signaldefinitionorstub() {
        return alf_signaldefinitionorstub;
    }

    public void setAlf_signaldefinitionorstub(alf_SignalDefinitionOrStub alf_signaldefinitionorstub) {
        this.alf_signaldefinitionorstub = alf_signaldefinitionorstub;
    }
    public alf_ClassifierSignature getAlf_classifiersignature() {
        return alf_classifiersignature;
    }

    public void setAlf_classifiersignature(alf_ClassifierSignature alf_classifiersignature) {
        this.alf_classifiersignature = alf_classifiersignature;
    }

}