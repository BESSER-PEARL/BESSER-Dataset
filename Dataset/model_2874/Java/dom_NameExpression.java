





import java.util.List;
import java.util.ArrayList;

public class dom_NameExpression extends Expression {

    private String name;





    private dom_ModelDeclarationParameter dom_modeldeclarationparameter;




    private dom_Annotation dom_annotation;




    private dom_OperationDefinition dom_operationdefinition;




    private dom_Program dom_program;


    public dom_NameExpression(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_ModelDeclarationParameter getDom_modeldeclarationparameter() {
        return dom_modeldeclarationparameter;
    }

    public void setDom_modeldeclarationparameter(dom_ModelDeclarationParameter dom_modeldeclarationparameter) {
        this.dom_modeldeclarationparameter = dom_modeldeclarationparameter;
    }
    public dom_Annotation getDom_annotation() {
        return dom_annotation;
    }

    public void setDom_annotation(dom_Annotation dom_annotation) {
        this.dom_annotation = dom_annotation;
    }
    public dom_OperationDefinition getDom_operationdefinition() {
        return dom_operationdefinition;
    }

    public void setDom_operationdefinition(dom_OperationDefinition dom_operationdefinition) {
        this.dom_operationdefinition = dom_operationdefinition;
    }
    public dom_Program getDom_program() {
        return dom_program;
    }

    public void setDom_program(dom_Program dom_program) {
        this.dom_program = dom_program;
    }

}