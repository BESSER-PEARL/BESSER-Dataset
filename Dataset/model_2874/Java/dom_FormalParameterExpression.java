





import java.util.List;
import java.util.ArrayList;

public class dom_FormalParameterExpression extends Expression {






    private dom_NameExpression dom_nameexpression;




    private dom_OperationDefinition dom_operationdefinition;




    private dom_FOLMethodCallExpression dom_folmethodcallexpression;


    public dom_FormalParameterExpression(
    ) {
        super(
        );
    }



    public dom_NameExpression getDom_nameexpression() {
        return dom_nameexpression;
    }

    public void setDom_nameexpression(dom_NameExpression dom_nameexpression) {
        this.dom_nameexpression = dom_nameexpression;
    }
    public dom_OperationDefinition getDom_operationdefinition() {
        return dom_operationdefinition;
    }

    public void setDom_operationdefinition(dom_OperationDefinition dom_operationdefinition) {
        this.dom_operationdefinition = dom_operationdefinition;
    }
    public dom_FOLMethodCallExpression getDom_folmethodcallexpression() {
        return dom_folmethodcallexpression;
    }

    public void setDom_folmethodcallexpression(dom_FOLMethodCallExpression dom_folmethodcallexpression) {
        this.dom_folmethodcallexpression = dom_folmethodcallexpression;
    }

}