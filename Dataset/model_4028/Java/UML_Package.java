





import java.util.List;
import java.util.ArrayList;

public class UML_Package extends PackageableElement {






    private UML_TypedElement uml_typedelement;




    private UML_TemplateParameterSubstitution uml_templateparametersubstitution;




    private UML_PackageableElement uml_packageableelement;




    private UML_TemplateBinding uml_templatebinding;


    public UML_Package(
    ) {
        super(
        );
    }



    public UML_TypedElement getUml_typedelement() {
        return uml_typedelement;
    }

    public void setUml_typedelement(UML_TypedElement uml_typedelement) {
        this.uml_typedelement = uml_typedelement;
    }
    public UML_TemplateParameterSubstitution getUml_templateparametersubstitution() {
        return uml_templateparametersubstitution;
    }

    public void setUml_templateparametersubstitution(UML_TemplateParameterSubstitution uml_templateparametersubstitution) {
        this.uml_templateparametersubstitution = uml_templateparametersubstitution;
    }
    public UML_PackageableElement getUml_packageableelement() {
        return uml_packageableelement;
    }

    public void setUml_packageableelement(UML_PackageableElement uml_packageableelement) {
        this.uml_packageableelement = uml_packageableelement;
    }
    public UML_TemplateBinding getUml_templatebinding() {
        return uml_templatebinding;
    }

    public void setUml_templatebinding(UML_TemplateBinding uml_templatebinding) {
        this.uml_templatebinding = uml_templatebinding;
    }

}