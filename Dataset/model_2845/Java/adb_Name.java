





import java.util.List;
import java.util.ArrayList;

public class adb_Name extends Interval {

    private String name;





    private adb_UnconstrainedIndexes adb_unconstrainedindexes;




    private adb_QualifiedName adb_qualifiedname;




    private adb_ParameterSpecification adb_parameterspecification;




    private adb_InterfaceList adb_interfacelist;




    private adb_ExceptionDeclaration adb_exceptiondeclaration;




    private adb_Allocator adb_allocator;




    private adb_AccessToDataInstance adb_accesstodatainstance;


    public adb_Name(
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

    public adb_UnconstrainedIndexes getAdb_unconstrainedindexes() {
        return adb_unconstrainedindexes;
    }

    public void setAdb_unconstrainedindexes(adb_UnconstrainedIndexes adb_unconstrainedindexes) {
        this.adb_unconstrainedindexes = adb_unconstrainedindexes;
    }
    public adb_QualifiedName getAdb_qualifiedname() {
        return adb_qualifiedname;
    }

    public void setAdb_qualifiedname(adb_QualifiedName adb_qualifiedname) {
        this.adb_qualifiedname = adb_qualifiedname;
    }
    public adb_ParameterSpecification getAdb_parameterspecification() {
        return adb_parameterspecification;
    }

    public void setAdb_parameterspecification(adb_ParameterSpecification adb_parameterspecification) {
        this.adb_parameterspecification = adb_parameterspecification;
    }
    public adb_InterfaceList getAdb_interfacelist() {
        return adb_interfacelist;
    }

    public void setAdb_interfacelist(adb_InterfaceList adb_interfacelist) {
        this.adb_interfacelist = adb_interfacelist;
    }
    public adb_ExceptionDeclaration getAdb_exceptiondeclaration() {
        return adb_exceptiondeclaration;
    }

    public void setAdb_exceptiondeclaration(adb_ExceptionDeclaration adb_exceptiondeclaration) {
        this.adb_exceptiondeclaration = adb_exceptiondeclaration;
    }
    public adb_Allocator getAdb_allocator() {
        return adb_allocator;
    }

    public void setAdb_allocator(adb_Allocator adb_allocator) {
        this.adb_allocator = adb_allocator;
    }
    public adb_AccessToDataInstance getAdb_accesstodatainstance() {
        return adb_accesstodatainstance;
    }

    public void setAdb_accesstodatainstance(adb_AccessToDataInstance adb_accesstodatainstance) {
        this.adb_accesstodatainstance = adb_accesstodatainstance;
    }

}