





import java.util.List;
import java.util.ArrayList;

public class miniJava_Expression extends Assignee, Statement {






    private miniJava_FieldAccess minijava_fieldaccess;




    private miniJava_Modulo minijava_modulo;




    private miniJava_Division minijava_division;




    private miniJava_SuperiorOrEqual minijava_superiororequal;




    private miniJava_ArrayAccess minijava_arrayaccess;




    private miniJava_Plus minijava_plus;




    private miniJava_Inferior minijava_inferior;




    private miniJava_And minijava_and;




    private miniJava_NewArray minijava_newarray;




    private miniJava_InferiorOrEqual minijava_inferiororequal;




    private miniJava_Superior minijava_superior;




    private miniJava_Inferior minijava_inferior;




    private miniJava_NewObject minijava_newobject;




    private miniJava_Superior minijava_superior;




    private miniJava_MethodCall minijava_methodcall;




    private miniJava_ArrayLength minijava_arraylength;




    private miniJava_Inequality minijava_inequality;




    private miniJava_Division minijava_division;




    private miniJava_And minijava_and;




    private miniJava_Multiplication minijava_multiplication;




    private miniJava_Minus minijava_minus;




    private miniJava_ForStatement minijava_forstatement;




    private miniJava_InferiorOrEqual minijava_inferiororequal;




    private miniJava_ArrayAccess minijava_arrayaccess;




    private miniJava_Equality minijava_equality;




    private miniJava_Equality minijava_equality;




    private miniJava_Or minijava_or;




    private miniJava_Or minijava_or;




    private miniJava_MethodCall minijava_methodcall;




    private miniJava_Multiplication minijava_multiplication;




    private miniJava_Field minijava_field;




    private miniJava_Modulo minijava_modulo;




    private miniJava_WhileStatement minijava_whilestatement;




    private miniJava_Inequality minijava_inequality;




    private miniJava_Not minijava_not;




    private miniJava_Neg minijava_neg;




    private miniJava_Plus minijava_plus;




    private miniJava_Minus minijava_minus;




    private miniJava_Assignment minijava_assignment;




    private miniJava_SuperiorOrEqual minijava_superiororequal;


    public miniJava_Expression(
    ) {
        super(
        );
    }



    public miniJava_FieldAccess getMinijava_fieldaccess() {
        return minijava_fieldaccess;
    }

    public void setMinijava_fieldaccess(miniJava_FieldAccess minijava_fieldaccess) {
        this.minijava_fieldaccess = minijava_fieldaccess;
    }
    public miniJava_Modulo getMinijava_modulo() {
        return minijava_modulo;
    }

    public void setMinijava_modulo(miniJava_Modulo minijava_modulo) {
        this.minijava_modulo = minijava_modulo;
    }
    public miniJava_Division getMinijava_division() {
        return minijava_division;
    }

    public void setMinijava_division(miniJava_Division minijava_division) {
        this.minijava_division = minijava_division;
    }
    public miniJava_SuperiorOrEqual getMinijava_superiororequal() {
        return minijava_superiororequal;
    }

    public void setMinijava_superiororequal(miniJava_SuperiorOrEqual minijava_superiororequal) {
        this.minijava_superiororequal = minijava_superiororequal;
    }
    public miniJava_ArrayAccess getMinijava_arrayaccess() {
        return minijava_arrayaccess;
    }

    public void setMinijava_arrayaccess(miniJava_ArrayAccess minijava_arrayaccess) {
        this.minijava_arrayaccess = minijava_arrayaccess;
    }
    public miniJava_Plus getMinijava_plus() {
        return minijava_plus;
    }

    public void setMinijava_plus(miniJava_Plus minijava_plus) {
        this.minijava_plus = minijava_plus;
    }
    public miniJava_Inferior getMinijava_inferior() {
        return minijava_inferior;
    }

    public void setMinijava_inferior(miniJava_Inferior minijava_inferior) {
        this.minijava_inferior = minijava_inferior;
    }
    public miniJava_And getMinijava_and() {
        return minijava_and;
    }

    public void setMinijava_and(miniJava_And minijava_and) {
        this.minijava_and = minijava_and;
    }
    public miniJava_NewArray getMinijava_newarray() {
        return minijava_newarray;
    }

    public void setMinijava_newarray(miniJava_NewArray minijava_newarray) {
        this.minijava_newarray = minijava_newarray;
    }
    public miniJava_InferiorOrEqual getMinijava_inferiororequal() {
        return minijava_inferiororequal;
    }

    public void setMinijava_inferiororequal(miniJava_InferiorOrEqual minijava_inferiororequal) {
        this.minijava_inferiororequal = minijava_inferiororequal;
    }
    public miniJava_Superior getMinijava_superior() {
        return minijava_superior;
    }

    public void setMinijava_superior(miniJava_Superior minijava_superior) {
        this.minijava_superior = minijava_superior;
    }
    public miniJava_Inferior getMinijava_inferior() {
        return minijava_inferior;
    }

    public void setMinijava_inferior(miniJava_Inferior minijava_inferior) {
        this.minijava_inferior = minijava_inferior;
    }
    public miniJava_NewObject getMinijava_newobject() {
        return minijava_newobject;
    }

    public void setMinijava_newobject(miniJava_NewObject minijava_newobject) {
        this.minijava_newobject = minijava_newobject;
    }
    public miniJava_Superior getMinijava_superior() {
        return minijava_superior;
    }

    public void setMinijava_superior(miniJava_Superior minijava_superior) {
        this.minijava_superior = minijava_superior;
    }
    public miniJava_MethodCall getMinijava_methodcall() {
        return minijava_methodcall;
    }

    public void setMinijava_methodcall(miniJava_MethodCall minijava_methodcall) {
        this.minijava_methodcall = minijava_methodcall;
    }
    public miniJava_ArrayLength getMinijava_arraylength() {
        return minijava_arraylength;
    }

    public void setMinijava_arraylength(miniJava_ArrayLength minijava_arraylength) {
        this.minijava_arraylength = minijava_arraylength;
    }
    public miniJava_Inequality getMinijava_inequality() {
        return minijava_inequality;
    }

    public void setMinijava_inequality(miniJava_Inequality minijava_inequality) {
        this.minijava_inequality = minijava_inequality;
    }
    public miniJava_Division getMinijava_division() {
        return minijava_division;
    }

    public void setMinijava_division(miniJava_Division minijava_division) {
        this.minijava_division = minijava_division;
    }
    public miniJava_And getMinijava_and() {
        return minijava_and;
    }

    public void setMinijava_and(miniJava_And minijava_and) {
        this.minijava_and = minijava_and;
    }
    public miniJava_Multiplication getMinijava_multiplication() {
        return minijava_multiplication;
    }

    public void setMinijava_multiplication(miniJava_Multiplication minijava_multiplication) {
        this.minijava_multiplication = minijava_multiplication;
    }
    public miniJava_Minus getMinijava_minus() {
        return minijava_minus;
    }

    public void setMinijava_minus(miniJava_Minus minijava_minus) {
        this.minijava_minus = minijava_minus;
    }
    public miniJava_ForStatement getMinijava_forstatement() {
        return minijava_forstatement;
    }

    public void setMinijava_forstatement(miniJava_ForStatement minijava_forstatement) {
        this.minijava_forstatement = minijava_forstatement;
    }
    public miniJava_InferiorOrEqual getMinijava_inferiororequal() {
        return minijava_inferiororequal;
    }

    public void setMinijava_inferiororequal(miniJava_InferiorOrEqual minijava_inferiororequal) {
        this.minijava_inferiororequal = minijava_inferiororequal;
    }
    public miniJava_ArrayAccess getMinijava_arrayaccess() {
        return minijava_arrayaccess;
    }

    public void setMinijava_arrayaccess(miniJava_ArrayAccess minijava_arrayaccess) {
        this.minijava_arrayaccess = minijava_arrayaccess;
    }
    public miniJava_Equality getMinijava_equality() {
        return minijava_equality;
    }

    public void setMinijava_equality(miniJava_Equality minijava_equality) {
        this.minijava_equality = minijava_equality;
    }
    public miniJava_Equality getMinijava_equality() {
        return minijava_equality;
    }

    public void setMinijava_equality(miniJava_Equality minijava_equality) {
        this.minijava_equality = minijava_equality;
    }
    public miniJava_Or getMinijava_or() {
        return minijava_or;
    }

    public void setMinijava_or(miniJava_Or minijava_or) {
        this.minijava_or = minijava_or;
    }
    public miniJava_Or getMinijava_or() {
        return minijava_or;
    }

    public void setMinijava_or(miniJava_Or minijava_or) {
        this.minijava_or = minijava_or;
    }
    public miniJava_MethodCall getMinijava_methodcall() {
        return minijava_methodcall;
    }

    public void setMinijava_methodcall(miniJava_MethodCall minijava_methodcall) {
        this.minijava_methodcall = minijava_methodcall;
    }
    public miniJava_Multiplication getMinijava_multiplication() {
        return minijava_multiplication;
    }

    public void setMinijava_multiplication(miniJava_Multiplication minijava_multiplication) {
        this.minijava_multiplication = minijava_multiplication;
    }
    public miniJava_Field getMinijava_field() {
        return minijava_field;
    }

    public void setMinijava_field(miniJava_Field minijava_field) {
        this.minijava_field = minijava_field;
    }
    public miniJava_Modulo getMinijava_modulo() {
        return minijava_modulo;
    }

    public void setMinijava_modulo(miniJava_Modulo minijava_modulo) {
        this.minijava_modulo = minijava_modulo;
    }
    public miniJava_WhileStatement getMinijava_whilestatement() {
        return minijava_whilestatement;
    }

    public void setMinijava_whilestatement(miniJava_WhileStatement minijava_whilestatement) {
        this.minijava_whilestatement = minijava_whilestatement;
    }
    public miniJava_Inequality getMinijava_inequality() {
        return minijava_inequality;
    }

    public void setMinijava_inequality(miniJava_Inequality minijava_inequality) {
        this.minijava_inequality = minijava_inequality;
    }
    public miniJava_Not getMinijava_not() {
        return minijava_not;
    }

    public void setMinijava_not(miniJava_Not minijava_not) {
        this.minijava_not = minijava_not;
    }
    public miniJava_Neg getMinijava_neg() {
        return minijava_neg;
    }

    public void setMinijava_neg(miniJava_Neg minijava_neg) {
        this.minijava_neg = minijava_neg;
    }
    public miniJava_Plus getMinijava_plus() {
        return minijava_plus;
    }

    public void setMinijava_plus(miniJava_Plus minijava_plus) {
        this.minijava_plus = minijava_plus;
    }
    public miniJava_Minus getMinijava_minus() {
        return minijava_minus;
    }

    public void setMinijava_minus(miniJava_Minus minijava_minus) {
        this.minijava_minus = minijava_minus;
    }
    public miniJava_Assignment getMinijava_assignment() {
        return minijava_assignment;
    }

    public void setMinijava_assignment(miniJava_Assignment minijava_assignment) {
        this.minijava_assignment = minijava_assignment;
    }
    public miniJava_SuperiorOrEqual getMinijava_superiororequal() {
        return minijava_superiororequal;
    }

    public void setMinijava_superiororequal(miniJava_SuperiorOrEqual minijava_superiororequal) {
        this.minijava_superiororequal = minijava_superiororequal;
    }

}