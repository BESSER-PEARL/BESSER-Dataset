





import java.util.List;
import java.util.ArrayList;

public class myAtl_ATLType  {

    private String modelName;





    private myAtl_RuleVariableDeclaration myatl_rulevariabledeclaration;




    private myAtl_ATLParameterCS myatl_atlparametercs;




    private myAtl_ATLDefCS myatl_atldefcs;


    public myAtl_ATLType(
        String modelName    ) {
        this.modelName = modelName;
    }


    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }

    public myAtl_RuleVariableDeclaration getMyatl_rulevariabledeclaration() {
        return myatl_rulevariabledeclaration;
    }

    public void setMyatl_rulevariabledeclaration(myAtl_RuleVariableDeclaration myatl_rulevariabledeclaration) {
        this.myatl_rulevariabledeclaration = myatl_rulevariabledeclaration;
    }
    public myAtl_ATLParameterCS getMyatl_atlparametercs() {
        return myatl_atlparametercs;
    }

    public void setMyatl_atlparametercs(myAtl_ATLParameterCS myatl_atlparametercs) {
        this.myatl_atlparametercs = myatl_atlparametercs;
    }
    public myAtl_ATLDefCS getMyatl_atldefcs() {
        return myatl_atldefcs;
    }

    public void setMyatl_atldefcs(myAtl_ATLDefCS myatl_atldefcs) {
        this.myatl_atldefcs = myatl_atldefcs;
    }

}