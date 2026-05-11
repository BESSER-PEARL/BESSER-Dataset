





import java.util.List;
import java.util.ArrayList;

public class alf_AssociationDeclaration  {

    private boolean isAbstract;





    private alf_AssociationDefinition alf_associationdefinition;




    private alf_ClassifierSignature alf_classifiersignature;




    private alf_AssociationDefinitionOrStub alf_associationdefinitionorstub;


    public alf_AssociationDeclaration(
        boolean isAbstract    ) {
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public alf_AssociationDefinition getAlf_associationdefinition() {
        return alf_associationdefinition;
    }

    public void setAlf_associationdefinition(alf_AssociationDefinition alf_associationdefinition) {
        this.alf_associationdefinition = alf_associationdefinition;
    }
    public alf_ClassifierSignature getAlf_classifiersignature() {
        return alf_classifiersignature;
    }

    public void setAlf_classifiersignature(alf_ClassifierSignature alf_classifiersignature) {
        this.alf_classifiersignature = alf_classifiersignature;
    }
    public alf_AssociationDefinitionOrStub getAlf_associationdefinitionorstub() {
        return alf_associationdefinitionorstub;
    }

    public void setAlf_associationdefinitionorstub(alf_AssociationDefinitionOrStub alf_associationdefinitionorstub) {
        this.alf_associationdefinitionorstub = alf_associationdefinitionorstub;
    }

}