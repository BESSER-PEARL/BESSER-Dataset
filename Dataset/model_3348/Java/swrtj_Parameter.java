





import java.util.List;
import java.util.ArrayList;

public class swrtj_Parameter  {

    private String name;





    private swrtj_Constructor swrtj_constructor;




    private swrtj_Block swrtj_block;




    private swrtj_ParameterReference swrtj_parameterreference;




    private swrtj_Method swrtj_method;


    public swrtj_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swrtj_Constructor getSwrtj_constructor() {
        return swrtj_constructor;
    }

    public void setSwrtj_constructor(swrtj_Constructor swrtj_constructor) {
        this.swrtj_constructor = swrtj_constructor;
    }
    public swrtj_Block getSwrtj_block() {
        return swrtj_block;
    }

    public void setSwrtj_block(swrtj_Block swrtj_block) {
        this.swrtj_block = swrtj_block;
    }
    public swrtj_ParameterReference getSwrtj_parameterreference() {
        return swrtj_parameterreference;
    }

    public void setSwrtj_parameterreference(swrtj_ParameterReference swrtj_parameterreference) {
        this.swrtj_parameterreference = swrtj_parameterreference;
    }
    public swrtj_Method getSwrtj_method() {
        return swrtj_method;
    }

    public void setSwrtj_method(swrtj_Method swrtj_method) {
        this.swrtj_method = swrtj_method;
    }

}