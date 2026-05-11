





import java.util.List;
import java.util.ArrayList;

public class aS3_Parameter  {

    private String anytype;
    private String name;





    private aS3_EObject as3_eobject;




    private aS3_InterfaceMethod as3_interfacemethod;


    public aS3_Parameter(
        String anytype,        String name    ) {
        this.anytype = anytype;
        this.name = name;
    }


    public String getAnytype() {
        return anytype;
    }

    public void setAnytype(String anytype) {
        this.anytype = anytype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aS3_EObject getAs3_eobject() {
        return as3_eobject;
    }

    public void setAs3_eobject(aS3_EObject as3_eobject) {
        this.as3_eobject = as3_eobject;
    }
    public aS3_InterfaceMethod getAs3_interfacemethod() {
        return as3_interfacemethod;
    }

    public void setAs3_interfacemethod(aS3_InterfaceMethod as3_interfacemethod) {
        this.as3_interfacemethod = as3_interfacemethod;
    }

}