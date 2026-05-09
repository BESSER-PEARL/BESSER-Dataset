





import java.util.List;
import java.util.ArrayList;

public class UMLModel_OutputPin extends Pin {






    private UMLModel_LoopNode umlmodel_loopnode;




    private UMLModel_ConditionalNode umlmodel_conditionalnode;




    private UMLModel_ReadStructuralFeatureAction umlmodel_readstructuralfeatureaction;




    private UMLModel_CreateObjectAction umlmodel_createobjectaction;




    private UMLModel_CreateLinkObjectAction umlmodel_createlinkobjectaction;


    public UMLModel_OutputPin(
    ) {
        super(
        );
    }



    public UMLModel_LoopNode getUmlmodel_loopnode() {
        return umlmodel_loopnode;
    }

    public void setUmlmodel_loopnode(UMLModel_LoopNode umlmodel_loopnode) {
        this.umlmodel_loopnode = umlmodel_loopnode;
    }
    public UMLModel_ConditionalNode getUmlmodel_conditionalnode() {
        return umlmodel_conditionalnode;
    }

    public void setUmlmodel_conditionalnode(UMLModel_ConditionalNode umlmodel_conditionalnode) {
        this.umlmodel_conditionalnode = umlmodel_conditionalnode;
    }
    public UMLModel_ReadStructuralFeatureAction getUmlmodel_readstructuralfeatureaction() {
        return umlmodel_readstructuralfeatureaction;
    }

    public void setUmlmodel_readstructuralfeatureaction(UMLModel_ReadStructuralFeatureAction umlmodel_readstructuralfeatureaction) {
        this.umlmodel_readstructuralfeatureaction = umlmodel_readstructuralfeatureaction;
    }
    public UMLModel_CreateObjectAction getUmlmodel_createobjectaction() {
        return umlmodel_createobjectaction;
    }

    public void setUmlmodel_createobjectaction(UMLModel_CreateObjectAction umlmodel_createobjectaction) {
        this.umlmodel_createobjectaction = umlmodel_createobjectaction;
    }
    public UMLModel_CreateLinkObjectAction getUmlmodel_createlinkobjectaction() {
        return umlmodel_createlinkobjectaction;
    }

    public void setUmlmodel_createlinkobjectaction(UMLModel_CreateLinkObjectAction umlmodel_createlinkobjectaction) {
        this.umlmodel_createlinkobjectaction = umlmodel_createlinkobjectaction;
    }

}