





import java.util.List;
import java.util.ArrayList;

public class OclExpression  {






    private ATL_ExpressionStat atl_expressionstat;




    private OCL_OclType ocl_ocltype;




    private ATL_BindingStat atl_bindingstat;




    private OCL_IfExp ocl_ifexp;




    private OCL_LetExp ocl_letexp;




    private OCL_VariableDeclaration ocl_variabledeclaration;




    private OCL_MapElement ocl_mapelement;




    private OCL_PropertyCallExp ocl_propertycallexp;




    private ATL_Binding atl_binding;




    private OCL_IfExp ocl_ifexp;




    private ATL_ForStat atl_forstat;




    private OCL_CollectionExp ocl_collectionexp;




    private ATL_Query atl_query;




    private OCL_MapElement ocl_mapelement;




    private ATL_SimpleOutPatternElement atl_simpleoutpatternelement;




    private ATL_IfStat atl_ifstat;




    private ATL_ForEachOutPatternElement atl_foreachoutpatternelement;




    private ATL_InPattern atl_inpattern;




    private OCL_OperationCallExp ocl_operationcallexp;




    private OCL_IfExp ocl_ifexp;




    private ATL_BindingStat atl_bindingstat;




    private OCL_LoopExp ocl_loopexp;


    public OclExpression(
    ) {
    }



    public ATL_ExpressionStat getAtl_expressionstat() {
        return atl_expressionstat;
    }

    public void setAtl_expressionstat(ATL_ExpressionStat atl_expressionstat) {
        this.atl_expressionstat = atl_expressionstat;
    }
    public OCL_OclType getOcl_ocltype() {
        return ocl_ocltype;
    }

    public void setOcl_ocltype(OCL_OclType ocl_ocltype) {
        this.ocl_ocltype = ocl_ocltype;
    }
    public ATL_BindingStat getAtl_bindingstat() {
        return atl_bindingstat;
    }

    public void setAtl_bindingstat(ATL_BindingStat atl_bindingstat) {
        this.atl_bindingstat = atl_bindingstat;
    }
    public OCL_IfExp getOcl_ifexp() {
        return ocl_ifexp;
    }

    public void setOcl_ifexp(OCL_IfExp ocl_ifexp) {
        this.ocl_ifexp = ocl_ifexp;
    }
    public OCL_LetExp getOcl_letexp() {
        return ocl_letexp;
    }

    public void setOcl_letexp(OCL_LetExp ocl_letexp) {
        this.ocl_letexp = ocl_letexp;
    }
    public OCL_VariableDeclaration getOcl_variabledeclaration() {
        return ocl_variabledeclaration;
    }

    public void setOcl_variabledeclaration(OCL_VariableDeclaration ocl_variabledeclaration) {
        this.ocl_variabledeclaration = ocl_variabledeclaration;
    }
    public OCL_MapElement getOcl_mapelement() {
        return ocl_mapelement;
    }

    public void setOcl_mapelement(OCL_MapElement ocl_mapelement) {
        this.ocl_mapelement = ocl_mapelement;
    }
    public OCL_PropertyCallExp getOcl_propertycallexp() {
        return ocl_propertycallexp;
    }

    public void setOcl_propertycallexp(OCL_PropertyCallExp ocl_propertycallexp) {
        this.ocl_propertycallexp = ocl_propertycallexp;
    }
    public ATL_Binding getAtl_binding() {
        return atl_binding;
    }

    public void setAtl_binding(ATL_Binding atl_binding) {
        this.atl_binding = atl_binding;
    }
    public OCL_IfExp getOcl_ifexp() {
        return ocl_ifexp;
    }

    public void setOcl_ifexp(OCL_IfExp ocl_ifexp) {
        this.ocl_ifexp = ocl_ifexp;
    }
    public ATL_ForStat getAtl_forstat() {
        return atl_forstat;
    }

    public void setAtl_forstat(ATL_ForStat atl_forstat) {
        this.atl_forstat = atl_forstat;
    }
    public OCL_CollectionExp getOcl_collectionexp() {
        return ocl_collectionexp;
    }

    public void setOcl_collectionexp(OCL_CollectionExp ocl_collectionexp) {
        this.ocl_collectionexp = ocl_collectionexp;
    }
    public ATL_Query getAtl_query() {
        return atl_query;
    }

    public void setAtl_query(ATL_Query atl_query) {
        this.atl_query = atl_query;
    }
    public OCL_MapElement getOcl_mapelement() {
        return ocl_mapelement;
    }

    public void setOcl_mapelement(OCL_MapElement ocl_mapelement) {
        this.ocl_mapelement = ocl_mapelement;
    }
    public ATL_SimpleOutPatternElement getAtl_simpleoutpatternelement() {
        return atl_simpleoutpatternelement;
    }

    public void setAtl_simpleoutpatternelement(ATL_SimpleOutPatternElement atl_simpleoutpatternelement) {
        this.atl_simpleoutpatternelement = atl_simpleoutpatternelement;
    }
    public ATL_IfStat getAtl_ifstat() {
        return atl_ifstat;
    }

    public void setAtl_ifstat(ATL_IfStat atl_ifstat) {
        this.atl_ifstat = atl_ifstat;
    }
    public ATL_ForEachOutPatternElement getAtl_foreachoutpatternelement() {
        return atl_foreachoutpatternelement;
    }

    public void setAtl_foreachoutpatternelement(ATL_ForEachOutPatternElement atl_foreachoutpatternelement) {
        this.atl_foreachoutpatternelement = atl_foreachoutpatternelement;
    }
    public ATL_InPattern getAtl_inpattern() {
        return atl_inpattern;
    }

    public void setAtl_inpattern(ATL_InPattern atl_inpattern) {
        this.atl_inpattern = atl_inpattern;
    }
    public OCL_OperationCallExp getOcl_operationcallexp() {
        return ocl_operationcallexp;
    }

    public void setOcl_operationcallexp(OCL_OperationCallExp ocl_operationcallexp) {
        this.ocl_operationcallexp = ocl_operationcallexp;
    }
    public OCL_IfExp getOcl_ifexp() {
        return ocl_ifexp;
    }

    public void setOcl_ifexp(OCL_IfExp ocl_ifexp) {
        this.ocl_ifexp = ocl_ifexp;
    }
    public ATL_BindingStat getAtl_bindingstat() {
        return atl_bindingstat;
    }

    public void setAtl_bindingstat(ATL_BindingStat atl_bindingstat) {
        this.atl_bindingstat = atl_bindingstat;
    }
    public OCL_LoopExp getOcl_loopexp() {
        return ocl_loopexp;
    }

    public void setOcl_loopexp(OCL_LoopExp ocl_loopexp) {
        this.ocl_loopexp = ocl_loopexp;
    }

}