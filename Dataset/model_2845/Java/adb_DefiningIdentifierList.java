





import java.util.List;
import java.util.ArrayList;

public class adb_DefiningIdentifierList  {

    private String name;





    private adb_ExceptionDeclaration adb_exceptiondeclaration;




    private adb_NumberDeclaration adb_numberdeclaration;




    private adb_ComponentDeclaration adb_componentdeclaration;




    private adb_FormalObjectDeclaration adb_formalobjectdeclaration;




    private adb_ParameterSpecification adb_parameterspecification;


    public adb_DefiningIdentifierList(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adb_ExceptionDeclaration getAdb_exceptiondeclaration() {
        return adb_exceptiondeclaration;
    }

    public void setAdb_exceptiondeclaration(adb_ExceptionDeclaration adb_exceptiondeclaration) {
        this.adb_exceptiondeclaration = adb_exceptiondeclaration;
    }
    public adb_NumberDeclaration getAdb_numberdeclaration() {
        return adb_numberdeclaration;
    }

    public void setAdb_numberdeclaration(adb_NumberDeclaration adb_numberdeclaration) {
        this.adb_numberdeclaration = adb_numberdeclaration;
    }
    public adb_ComponentDeclaration getAdb_componentdeclaration() {
        return adb_componentdeclaration;
    }

    public void setAdb_componentdeclaration(adb_ComponentDeclaration adb_componentdeclaration) {
        this.adb_componentdeclaration = adb_componentdeclaration;
    }
    public adb_FormalObjectDeclaration getAdb_formalobjectdeclaration() {
        return adb_formalobjectdeclaration;
    }

    public void setAdb_formalobjectdeclaration(adb_FormalObjectDeclaration adb_formalobjectdeclaration) {
        this.adb_formalobjectdeclaration = adb_formalobjectdeclaration;
    }
    public adb_ParameterSpecification getAdb_parameterspecification() {
        return adb_parameterspecification;
    }

    public void setAdb_parameterspecification(adb_ParameterSpecification adb_parameterspecification) {
        this.adb_parameterspecification = adb_parameterspecification;
    }

}