





import java.util.List;
import java.util.ArrayList;

public class java_Parameter_list_method_call  {

    private String name;
    private String parameters;





    private java_Method_call java_method_call;


    public java_Parameter_list_method_call(
        String name,        String parameters    ) {
        this.name = name;
        this.parameters = parameters;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public java_Method_call getJava_method_call() {
        return java_method_call;
    }

    public void setJava_method_call(java_Method_call java_method_call) {
        this.java_method_call = java_method_call;
    }

}