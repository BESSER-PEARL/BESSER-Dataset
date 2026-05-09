





import java.util.List;
import java.util.ArrayList;

public class cjsidl_serviceDef  {

    private String serviceName;
    private String serviceVersion;
    private String assumpt;
    private String name;





    private cjsidl_declaredConstSet cjsidl_declaredconstset;




    private cjsidl_references cjsidl_references;




    private cjsidl_description cjsidl_description;




    private cjsidl_messageSet cjsidl_messageset;




    private cjsidl_protocolBehavior cjsidl_protocolbehavior;




    private cjsidl_refAttr cjsidl_refattr;




    private cjsidl_internalEventSet cjsidl_internaleventset;




    private cjsidl_declaredTypeSet cjsidl_declaredtypeset;


    public cjsidl_serviceDef(
        String serviceName,        String serviceVersion,        String assumpt,        String name    ) {
        this.serviceName = serviceName;
        this.serviceVersion = serviceVersion;
        this.assumpt = assumpt;
        this.name = name;
    }


    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }
    public String getServiceversion() {
        return serviceVersion;
    }

    public void setServiceversion(String serviceVersion) {
        this.serviceVersion = serviceVersion;
    }
    public String getAssumpt() {
        return assumpt;
    }

    public void setAssumpt(String assumpt) {
        this.assumpt = assumpt;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cjsidl_declaredConstSet getCjsidl_declaredconstset() {
        return cjsidl_declaredconstset;
    }

    public void setCjsidl_declaredconstset(cjsidl_declaredConstSet cjsidl_declaredconstset) {
        this.cjsidl_declaredconstset = cjsidl_declaredconstset;
    }
    public cjsidl_references getCjsidl_references() {
        return cjsidl_references;
    }

    public void setCjsidl_references(cjsidl_references cjsidl_references) {
        this.cjsidl_references = cjsidl_references;
    }
    public cjsidl_description getCjsidl_description() {
        return cjsidl_description;
    }

    public void setCjsidl_description(cjsidl_description cjsidl_description) {
        this.cjsidl_description = cjsidl_description;
    }
    public cjsidl_messageSet getCjsidl_messageset() {
        return cjsidl_messageset;
    }

    public void setCjsidl_messageset(cjsidl_messageSet cjsidl_messageset) {
        this.cjsidl_messageset = cjsidl_messageset;
    }
    public cjsidl_protocolBehavior getCjsidl_protocolbehavior() {
        return cjsidl_protocolbehavior;
    }

    public void setCjsidl_protocolbehavior(cjsidl_protocolBehavior cjsidl_protocolbehavior) {
        this.cjsidl_protocolbehavior = cjsidl_protocolbehavior;
    }
    public cjsidl_refAttr getCjsidl_refattr() {
        return cjsidl_refattr;
    }

    public void setCjsidl_refattr(cjsidl_refAttr cjsidl_refattr) {
        this.cjsidl_refattr = cjsidl_refattr;
    }
    public cjsidl_internalEventSet getCjsidl_internaleventset() {
        return cjsidl_internaleventset;
    }

    public void setCjsidl_internaleventset(cjsidl_internalEventSet cjsidl_internaleventset) {
        this.cjsidl_internaleventset = cjsidl_internaleventset;
    }
    public cjsidl_declaredTypeSet getCjsidl_declaredtypeset() {
        return cjsidl_declaredtypeset;
    }

    public void setCjsidl_declaredtypeset(cjsidl_declaredTypeSet cjsidl_declaredtypeset) {
        this.cjsidl_declaredtypeset = cjsidl_declaredtypeset;
    }

}