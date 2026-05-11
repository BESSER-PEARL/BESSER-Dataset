





import java.util.List;
import java.util.ArrayList;

public class aS3_AccessorRole  {

    private String accessor;





    private aS3_InterfaceMethod as3_interfacemethod;


    public aS3_AccessorRole(
        String accessor    ) {
        this.accessor = accessor;
    }


    public String getAccessor() {
        return accessor;
    }

    public void setAccessor(String accessor) {
        this.accessor = accessor;
    }

    public aS3_InterfaceMethod getAs3_interfacemethod() {
        return as3_interfacemethod;
    }

    public void setAs3_interfacemethod(aS3_InterfaceMethod as3_interfacemethod) {
        this.as3_interfacemethod = as3_interfacemethod;
    }

}