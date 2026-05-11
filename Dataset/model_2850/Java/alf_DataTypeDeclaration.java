





import java.util.List;
import java.util.ArrayList;

public class alf_DataTypeDeclaration  {

    private boolean isAbstract;





    private alf_DataTypeDefinitionOrStub alf_datatypedefinitionorstub;




    private alf_DataTypeDefinition alf_datatypedefinition;




    private alf_ClassifierSignature alf_classifiersignature;


    public alf_DataTypeDeclaration(
        boolean isAbstract    ) {
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public alf_DataTypeDefinitionOrStub getAlf_datatypedefinitionorstub() {
        return alf_datatypedefinitionorstub;
    }

    public void setAlf_datatypedefinitionorstub(alf_DataTypeDefinitionOrStub alf_datatypedefinitionorstub) {
        this.alf_datatypedefinitionorstub = alf_datatypedefinitionorstub;
    }
    public alf_DataTypeDefinition getAlf_datatypedefinition() {
        return alf_datatypedefinition;
    }

    public void setAlf_datatypedefinition(alf_DataTypeDefinition alf_datatypedefinition) {
        this.alf_datatypedefinition = alf_datatypedefinition;
    }
    public alf_ClassifierSignature getAlf_classifiersignature() {
        return alf_classifiersignature;
    }

    public void setAlf_classifiersignature(alf_ClassifierSignature alf_classifiersignature) {
        this.alf_classifiersignature = alf_classifiersignature;
    }

}