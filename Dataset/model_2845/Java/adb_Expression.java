





import java.util.List;
import java.util.ArrayList;

public class adb_Expression extends ExplicitGenericActualParameter, DiscreteChoice, EntryIndex, AncestorPart, ParameterEffectiveValue {

    private String booleanOperator;





    private adb_ComponentDeclaration adb_componentdeclaration;




    private adb_ParameterSpecification adb_parameterspecification;




    private adb_ComponentClause adb_componentclause;




    private adb_FixedPointDefinition adb_fixedpointdefinition;




    private adb_AspectClause adb_aspectclause;




    private adb_RealTypeDefinition adb_realtypedefinition;




    private adb_ModularTypeDefinition adb_modulartypedefinition;




    private adb_ModClause adb_modclause;




    private adb_NumberDeclaration adb_numberdeclaration;


    public adb_Expression(
        String booleanOperator    ) {
        super(
        );
        this.booleanOperator = booleanOperator;
    }


    public String getBooleanoperator() {
        return booleanOperator;
    }

    public void setBooleanoperator(String booleanOperator) {
        this.booleanOperator = booleanOperator;
    }

    public adb_ComponentDeclaration getAdb_componentdeclaration() {
        return adb_componentdeclaration;
    }

    public void setAdb_componentdeclaration(adb_ComponentDeclaration adb_componentdeclaration) {
        this.adb_componentdeclaration = adb_componentdeclaration;
    }
    public adb_ParameterSpecification getAdb_parameterspecification() {
        return adb_parameterspecification;
    }

    public void setAdb_parameterspecification(adb_ParameterSpecification adb_parameterspecification) {
        this.adb_parameterspecification = adb_parameterspecification;
    }
    public adb_ComponentClause getAdb_componentclause() {
        return adb_componentclause;
    }

    public void setAdb_componentclause(adb_ComponentClause adb_componentclause) {
        this.adb_componentclause = adb_componentclause;
    }
    public adb_FixedPointDefinition getAdb_fixedpointdefinition() {
        return adb_fixedpointdefinition;
    }

    public void setAdb_fixedpointdefinition(adb_FixedPointDefinition adb_fixedpointdefinition) {
        this.adb_fixedpointdefinition = adb_fixedpointdefinition;
    }
    public adb_AspectClause getAdb_aspectclause() {
        return adb_aspectclause;
    }

    public void setAdb_aspectclause(adb_AspectClause adb_aspectclause) {
        this.adb_aspectclause = adb_aspectclause;
    }
    public adb_RealTypeDefinition getAdb_realtypedefinition() {
        return adb_realtypedefinition;
    }

    public void setAdb_realtypedefinition(adb_RealTypeDefinition adb_realtypedefinition) {
        this.adb_realtypedefinition = adb_realtypedefinition;
    }
    public adb_ModularTypeDefinition getAdb_modulartypedefinition() {
        return adb_modulartypedefinition;
    }

    public void setAdb_modulartypedefinition(adb_ModularTypeDefinition adb_modulartypedefinition) {
        this.adb_modulartypedefinition = adb_modulartypedefinition;
    }
    public adb_ModClause getAdb_modclause() {
        return adb_modclause;
    }

    public void setAdb_modclause(adb_ModClause adb_modclause) {
        this.adb_modclause = adb_modclause;
    }
    public adb_NumberDeclaration getAdb_numberdeclaration() {
        return adb_numberdeclaration;
    }

    public void setAdb_numberdeclaration(adb_NumberDeclaration adb_numberdeclaration) {
        this.adb_numberdeclaration = adb_numberdeclaration;
    }

}