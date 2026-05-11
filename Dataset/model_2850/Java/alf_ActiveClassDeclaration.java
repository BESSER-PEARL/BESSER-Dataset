





import java.util.List;
import java.util.ArrayList;

public class alf_ActiveClassDeclaration  {

    private boolean isAbstract;





    private alf_ActiveClassDefinitionOrStub alf_activeclassdefinitionorstub;




    private alf_ActiveClassDefinition alf_activeclassdefinition;




    private alf_ClassifierSignature alf_classifiersignature;


    public alf_ActiveClassDeclaration(
        boolean isAbstract    ) {
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public alf_ActiveClassDefinitionOrStub getAlf_activeclassdefinitionorstub() {
        return alf_activeclassdefinitionorstub;
    }

    public void setAlf_activeclassdefinitionorstub(alf_ActiveClassDefinitionOrStub alf_activeclassdefinitionorstub) {
        this.alf_activeclassdefinitionorstub = alf_activeclassdefinitionorstub;
    }
    public alf_ActiveClassDefinition getAlf_activeclassdefinition() {
        return alf_activeclassdefinition;
    }

    public void setAlf_activeclassdefinition(alf_ActiveClassDefinition alf_activeclassdefinition) {
        this.alf_activeclassdefinition = alf_activeclassdefinition;
    }
    public alf_ClassifierSignature getAlf_classifiersignature() {
        return alf_classifiersignature;
    }

    public void setAlf_classifiersignature(alf_ClassifierSignature alf_classifiersignature) {
        this.alf_classifiersignature = alf_classifiersignature;
    }

}