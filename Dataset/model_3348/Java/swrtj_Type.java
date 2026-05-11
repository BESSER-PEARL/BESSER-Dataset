





import java.util.List;
import java.util.ArrayList;

public class swrtj_Type  {

    private String primitiveType;





    private swrtj_Cast swrtj_cast;




    private swrtj_Parameter swrtj_parameter;




    private swrtj_Interface swrtj_interface;




    private swrtj_Method swrtj_method;




    private swrtj_Field swrtj_field;


    public swrtj_Type(
        String primitiveType    ) {
        this.primitiveType = primitiveType;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }

    public swrtj_Cast getSwrtj_cast() {
        return swrtj_cast;
    }

    public void setSwrtj_cast(swrtj_Cast swrtj_cast) {
        this.swrtj_cast = swrtj_cast;
    }
    public swrtj_Parameter getSwrtj_parameter() {
        return swrtj_parameter;
    }

    public void setSwrtj_parameter(swrtj_Parameter swrtj_parameter) {
        this.swrtj_parameter = swrtj_parameter;
    }
    public swrtj_Interface getSwrtj_interface() {
        return swrtj_interface;
    }

    public void setSwrtj_interface(swrtj_Interface swrtj_interface) {
        this.swrtj_interface = swrtj_interface;
    }
    public swrtj_Method getSwrtj_method() {
        return swrtj_method;
    }

    public void setSwrtj_method(swrtj_Method swrtj_method) {
        this.swrtj_method = swrtj_method;
    }
    public swrtj_Field getSwrtj_field() {
        return swrtj_field;
    }

    public void setSwrtj_field(swrtj_Field swrtj_field) {
        this.swrtj_field = swrtj_field;
    }

}