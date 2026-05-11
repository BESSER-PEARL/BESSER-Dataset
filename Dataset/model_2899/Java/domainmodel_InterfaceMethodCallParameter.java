





import java.util.List;
import java.util.ArrayList;

public class domainmodel_InterfaceMethodCallParameter  {

    private String parameterType;





    private domainmodel_MethodParameter domainmodel_methodparameter;




    private domainmodel_InterfaceMethodCallParameters domainmodel_interfacemethodcallparameters;


    public domainmodel_InterfaceMethodCallParameter(
        String parameterType    ) {
        this.parameterType = parameterType;
    }


    public String getParametertype() {
        return parameterType;
    }

    public void setParametertype(String parameterType) {
        this.parameterType = parameterType;
    }

    public domainmodel_MethodParameter getDomainmodel_methodparameter() {
        return domainmodel_methodparameter;
    }

    public void setDomainmodel_methodparameter(domainmodel_MethodParameter domainmodel_methodparameter) {
        this.domainmodel_methodparameter = domainmodel_methodparameter;
    }
    public domainmodel_InterfaceMethodCallParameters getDomainmodel_interfacemethodcallparameters() {
        return domainmodel_interfacemethodcallparameters;
    }

    public void setDomainmodel_interfacemethodcallparameters(domainmodel_InterfaceMethodCallParameters domainmodel_interfacemethodcallparameters) {
        this.domainmodel_interfacemethodcallparameters = domainmodel_interfacemethodcallparameters;
    }

}