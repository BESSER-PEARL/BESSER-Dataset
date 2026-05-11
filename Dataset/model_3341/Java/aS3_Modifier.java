





import java.util.List;
import java.util.ArrayList;

public class aS3_Modifier  {

    private String access;
    private boolean static;
    private boolean final;
    private boolean dynamic;
    private boolean native;





    private aS3_InterfaceMethod as3_interfacemethod;


    public aS3_Modifier(
        String access,        boolean static,        boolean final,        boolean dynamic,        boolean native    ) {
        this.access = access;
        this.static = static;
        this.final = final;
        this.dynamic = dynamic;
        this.native = native;
    }


    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getDynamic() {
        return dynamic;
    }

    public void setDynamic(boolean dynamic) {
        this.dynamic = dynamic;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }

    public aS3_InterfaceMethod getAs3_interfacemethod() {
        return as3_interfacemethod;
    }

    public void setAs3_interfacemethod(aS3_InterfaceMethod as3_interfacemethod) {
        this.as3_interfacemethod = as3_interfacemethod;
    }

}