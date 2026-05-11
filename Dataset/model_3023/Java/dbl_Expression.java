





import java.util.List;
import java.util.ArrayList;

public class dbl_Expression extends Construct {






    private dbl_Variable dbl_variable;




    private dbl_ForEachStatement dbl_foreachstatement;




    private dbl_QuotedExpression dbl_quotedexpression;




    private dbl_MappingStatement dbl_mappingstatement;




    private dbl_BinaryOperator dbl_binaryoperator;




    private dbl_Mapping dbl_mapping;




    private dbl_KeyValuePair dbl_keyvaluepair;




    private dbl_SetGenContextStatement dbl_setgencontextstatement;




    private dbl_Clazz dbl_clazz;




    private dbl_IncludePattern dbl_includepattern;




    private dbl_ResumeGenStatement dbl_resumegenstatement;




    private dbl_MetaExpr dbl_metaexpr;




    private dbl_ExpandStatement dbl_expandstatement;




    private dbl_DynamicMappingPart dbl_dynamicmappingpart;




    private dbl_ArgumentExpression dbl_argumentexpression;




    private dbl_EvalExpr dbl_evalexpr;




    private dbl_ExpandStatement dbl_expandstatement;




    private dbl_UnaryOperator dbl_unaryoperator;




    private dbl_BinaryOperator dbl_binaryoperator;




    private dbl_SetOp dbl_setop;




    private dbl_SaveGenStatement dbl_savegenstatement;




    private dbl_ConsiderIdElements dbl_consideridelements;




    private dbl_ExpandExpression dbl_expandexpression;


    public dbl_Expression(
    ) {
        super(
        );
    }



    public dbl_Variable getDbl_variable() {
        return dbl_variable;
    }

    public void setDbl_variable(dbl_Variable dbl_variable) {
        this.dbl_variable = dbl_variable;
    }
    public dbl_ForEachStatement getDbl_foreachstatement() {
        return dbl_foreachstatement;
    }

    public void setDbl_foreachstatement(dbl_ForEachStatement dbl_foreachstatement) {
        this.dbl_foreachstatement = dbl_foreachstatement;
    }
    public dbl_QuotedExpression getDbl_quotedexpression() {
        return dbl_quotedexpression;
    }

    public void setDbl_quotedexpression(dbl_QuotedExpression dbl_quotedexpression) {
        this.dbl_quotedexpression = dbl_quotedexpression;
    }
    public dbl_MappingStatement getDbl_mappingstatement() {
        return dbl_mappingstatement;
    }

    public void setDbl_mappingstatement(dbl_MappingStatement dbl_mappingstatement) {
        this.dbl_mappingstatement = dbl_mappingstatement;
    }
    public dbl_BinaryOperator getDbl_binaryoperator() {
        return dbl_binaryoperator;
    }

    public void setDbl_binaryoperator(dbl_BinaryOperator dbl_binaryoperator) {
        this.dbl_binaryoperator = dbl_binaryoperator;
    }
    public dbl_Mapping getDbl_mapping() {
        return dbl_mapping;
    }

    public void setDbl_mapping(dbl_Mapping dbl_mapping) {
        this.dbl_mapping = dbl_mapping;
    }
    public dbl_KeyValuePair getDbl_keyvaluepair() {
        return dbl_keyvaluepair;
    }

    public void setDbl_keyvaluepair(dbl_KeyValuePair dbl_keyvaluepair) {
        this.dbl_keyvaluepair = dbl_keyvaluepair;
    }
    public dbl_SetGenContextStatement getDbl_setgencontextstatement() {
        return dbl_setgencontextstatement;
    }

    public void setDbl_setgencontextstatement(dbl_SetGenContextStatement dbl_setgencontextstatement) {
        this.dbl_setgencontextstatement = dbl_setgencontextstatement;
    }
    public dbl_Clazz getDbl_clazz() {
        return dbl_clazz;
    }

    public void setDbl_clazz(dbl_Clazz dbl_clazz) {
        this.dbl_clazz = dbl_clazz;
    }
    public dbl_IncludePattern getDbl_includepattern() {
        return dbl_includepattern;
    }

    public void setDbl_includepattern(dbl_IncludePattern dbl_includepattern) {
        this.dbl_includepattern = dbl_includepattern;
    }
    public dbl_ResumeGenStatement getDbl_resumegenstatement() {
        return dbl_resumegenstatement;
    }

    public void setDbl_resumegenstatement(dbl_ResumeGenStatement dbl_resumegenstatement) {
        this.dbl_resumegenstatement = dbl_resumegenstatement;
    }
    public dbl_MetaExpr getDbl_metaexpr() {
        return dbl_metaexpr;
    }

    public void setDbl_metaexpr(dbl_MetaExpr dbl_metaexpr) {
        this.dbl_metaexpr = dbl_metaexpr;
    }
    public dbl_ExpandStatement getDbl_expandstatement() {
        return dbl_expandstatement;
    }

    public void setDbl_expandstatement(dbl_ExpandStatement dbl_expandstatement) {
        this.dbl_expandstatement = dbl_expandstatement;
    }
    public dbl_DynamicMappingPart getDbl_dynamicmappingpart() {
        return dbl_dynamicmappingpart;
    }

    public void setDbl_dynamicmappingpart(dbl_DynamicMappingPart dbl_dynamicmappingpart) {
        this.dbl_dynamicmappingpart = dbl_dynamicmappingpart;
    }
    public dbl_ArgumentExpression getDbl_argumentexpression() {
        return dbl_argumentexpression;
    }

    public void setDbl_argumentexpression(dbl_ArgumentExpression dbl_argumentexpression) {
        this.dbl_argumentexpression = dbl_argumentexpression;
    }
    public dbl_EvalExpr getDbl_evalexpr() {
        return dbl_evalexpr;
    }

    public void setDbl_evalexpr(dbl_EvalExpr dbl_evalexpr) {
        this.dbl_evalexpr = dbl_evalexpr;
    }
    public dbl_ExpandStatement getDbl_expandstatement() {
        return dbl_expandstatement;
    }

    public void setDbl_expandstatement(dbl_ExpandStatement dbl_expandstatement) {
        this.dbl_expandstatement = dbl_expandstatement;
    }
    public dbl_UnaryOperator getDbl_unaryoperator() {
        return dbl_unaryoperator;
    }

    public void setDbl_unaryoperator(dbl_UnaryOperator dbl_unaryoperator) {
        this.dbl_unaryoperator = dbl_unaryoperator;
    }
    public dbl_BinaryOperator getDbl_binaryoperator() {
        return dbl_binaryoperator;
    }

    public void setDbl_binaryoperator(dbl_BinaryOperator dbl_binaryoperator) {
        this.dbl_binaryoperator = dbl_binaryoperator;
    }
    public dbl_SetOp getDbl_setop() {
        return dbl_setop;
    }

    public void setDbl_setop(dbl_SetOp dbl_setop) {
        this.dbl_setop = dbl_setop;
    }
    public dbl_SaveGenStatement getDbl_savegenstatement() {
        return dbl_savegenstatement;
    }

    public void setDbl_savegenstatement(dbl_SaveGenStatement dbl_savegenstatement) {
        this.dbl_savegenstatement = dbl_savegenstatement;
    }
    public dbl_ConsiderIdElements getDbl_consideridelements() {
        return dbl_consideridelements;
    }

    public void setDbl_consideridelements(dbl_ConsiderIdElements dbl_consideridelements) {
        this.dbl_consideridelements = dbl_consideridelements;
    }
    public dbl_ExpandExpression getDbl_expandexpression() {
        return dbl_expandexpression;
    }

    public void setDbl_expandexpression(dbl_ExpandExpression dbl_expandexpression) {
        this.dbl_expandexpression = dbl_expandexpression;
    }

}