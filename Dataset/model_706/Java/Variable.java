





import java.util.List;
import java.util.ArrayList;

public class Variable  {






    private FlatQVT_LetExp flatqvt_letexp;




    private FlatQVT_ResolveExp flatqvt_resolveexp;




    private FlatQVT_UnpackExp flatqvt_unpackexp;




    private FlatQVT_TemplateExp flatqvt_templateexp;




    private FlatQVT_Pattern flatqvt_pattern;




    private FlatQVT_CollectionTemplateExp flatqvt_collectiontemplateexp;




    private FlatQVT_InstantiationExp flatqvt_instantiationexp;




    private FlatQVT_LoopExp flatqvt_loopexp;




    private FlatQVT_ExpressionInOcl flatqvt_expressioninocl;




    private FlatQVT_RelationDomainAssignment flatqvt_relationdomainassignment;




    private FlatQVT_VariableExp flatqvt_variableexp;




    private FlatQVT_OperationBody flatqvt_operationbody;




    private FlatQVT_ComputeExp flatqvt_computeexp;




    private FlatQVT_VariableInitExp flatqvt_variableinitexp;




    private FlatQVT_ExpressionInOcl flatqvt_expressioninocl;




    private FlatQVT_VariableAssignment flatqvt_variableassignment;




    private FlatQVT_Module flatqvt_module;




    private FlatQVT_ExpressionInOcl flatqvt_expressioninocl;


    public Variable(
    ) {
    }



    public FlatQVT_LetExp getFlatqvt_letexp() {
        return flatqvt_letexp;
    }

    public void setFlatqvt_letexp(FlatQVT_LetExp flatqvt_letexp) {
        this.flatqvt_letexp = flatqvt_letexp;
    }
    public FlatQVT_ResolveExp getFlatqvt_resolveexp() {
        return flatqvt_resolveexp;
    }

    public void setFlatqvt_resolveexp(FlatQVT_ResolveExp flatqvt_resolveexp) {
        this.flatqvt_resolveexp = flatqvt_resolveexp;
    }
    public FlatQVT_UnpackExp getFlatqvt_unpackexp() {
        return flatqvt_unpackexp;
    }

    public void setFlatqvt_unpackexp(FlatQVT_UnpackExp flatqvt_unpackexp) {
        this.flatqvt_unpackexp = flatqvt_unpackexp;
    }
    public FlatQVT_TemplateExp getFlatqvt_templateexp() {
        return flatqvt_templateexp;
    }

    public void setFlatqvt_templateexp(FlatQVT_TemplateExp flatqvt_templateexp) {
        this.flatqvt_templateexp = flatqvt_templateexp;
    }
    public FlatQVT_Pattern getFlatqvt_pattern() {
        return flatqvt_pattern;
    }

    public void setFlatqvt_pattern(FlatQVT_Pattern flatqvt_pattern) {
        this.flatqvt_pattern = flatqvt_pattern;
    }
    public FlatQVT_CollectionTemplateExp getFlatqvt_collectiontemplateexp() {
        return flatqvt_collectiontemplateexp;
    }

    public void setFlatqvt_collectiontemplateexp(FlatQVT_CollectionTemplateExp flatqvt_collectiontemplateexp) {
        this.flatqvt_collectiontemplateexp = flatqvt_collectiontemplateexp;
    }
    public FlatQVT_InstantiationExp getFlatqvt_instantiationexp() {
        return flatqvt_instantiationexp;
    }

    public void setFlatqvt_instantiationexp(FlatQVT_InstantiationExp flatqvt_instantiationexp) {
        this.flatqvt_instantiationexp = flatqvt_instantiationexp;
    }
    public FlatQVT_LoopExp getFlatqvt_loopexp() {
        return flatqvt_loopexp;
    }

    public void setFlatqvt_loopexp(FlatQVT_LoopExp flatqvt_loopexp) {
        this.flatqvt_loopexp = flatqvt_loopexp;
    }
    public FlatQVT_ExpressionInOcl getFlatqvt_expressioninocl() {
        return flatqvt_expressioninocl;
    }

    public void setFlatqvt_expressioninocl(FlatQVT_ExpressionInOcl flatqvt_expressioninocl) {
        this.flatqvt_expressioninocl = flatqvt_expressioninocl;
    }
    public FlatQVT_RelationDomainAssignment getFlatqvt_relationdomainassignment() {
        return flatqvt_relationdomainassignment;
    }

    public void setFlatqvt_relationdomainassignment(FlatQVT_RelationDomainAssignment flatqvt_relationdomainassignment) {
        this.flatqvt_relationdomainassignment = flatqvt_relationdomainassignment;
    }
    public FlatQVT_VariableExp getFlatqvt_variableexp() {
        return flatqvt_variableexp;
    }

    public void setFlatqvt_variableexp(FlatQVT_VariableExp flatqvt_variableexp) {
        this.flatqvt_variableexp = flatqvt_variableexp;
    }
    public FlatQVT_OperationBody getFlatqvt_operationbody() {
        return flatqvt_operationbody;
    }

    public void setFlatqvt_operationbody(FlatQVT_OperationBody flatqvt_operationbody) {
        this.flatqvt_operationbody = flatqvt_operationbody;
    }
    public FlatQVT_ComputeExp getFlatqvt_computeexp() {
        return flatqvt_computeexp;
    }

    public void setFlatqvt_computeexp(FlatQVT_ComputeExp flatqvt_computeexp) {
        this.flatqvt_computeexp = flatqvt_computeexp;
    }
    public FlatQVT_VariableInitExp getFlatqvt_variableinitexp() {
        return flatqvt_variableinitexp;
    }

    public void setFlatqvt_variableinitexp(FlatQVT_VariableInitExp flatqvt_variableinitexp) {
        this.flatqvt_variableinitexp = flatqvt_variableinitexp;
    }
    public FlatQVT_ExpressionInOcl getFlatqvt_expressioninocl() {
        return flatqvt_expressioninocl;
    }

    public void setFlatqvt_expressioninocl(FlatQVT_ExpressionInOcl flatqvt_expressioninocl) {
        this.flatqvt_expressioninocl = flatqvt_expressioninocl;
    }
    public FlatQVT_VariableAssignment getFlatqvt_variableassignment() {
        return flatqvt_variableassignment;
    }

    public void setFlatqvt_variableassignment(FlatQVT_VariableAssignment flatqvt_variableassignment) {
        this.flatqvt_variableassignment = flatqvt_variableassignment;
    }
    public FlatQVT_Module getFlatqvt_module() {
        return flatqvt_module;
    }

    public void setFlatqvt_module(FlatQVT_Module flatqvt_module) {
        this.flatqvt_module = flatqvt_module;
    }
    public FlatQVT_ExpressionInOcl getFlatqvt_expressioninocl() {
        return flatqvt_expressioninocl;
    }

    public void setFlatqvt_expressioninocl(FlatQVT_ExpressionInOcl flatqvt_expressioninocl) {
        this.flatqvt_expressioninocl = flatqvt_expressioninocl;
    }

}