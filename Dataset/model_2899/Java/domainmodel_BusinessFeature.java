





import java.util.List;
import java.util.ArrayList;

public class domainmodel_BusinessFeature  {

    private String name;
    private String connectPoint1;
    private String connectEnd;





    private domainmodel_InterfaceMethodCall domainmodel_interfacemethodcall;




    private domainmodel_BusinessFeature domainmodel_businessfeature;


    public domainmodel_BusinessFeature(
        String name,        String connectPoint1,        String connectEnd    ) {
        this.name = name;
        this.connectPoint1 = connectPoint1;
        this.connectEnd = connectEnd;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConnectpoint1() {
        return connectPoint1;
    }

    public void setConnectpoint1(String connectPoint1) {
        this.connectPoint1 = connectPoint1;
    }
    public String getConnectend() {
        return connectEnd;
    }

    public void setConnectend(String connectEnd) {
        this.connectEnd = connectEnd;
    }

    public domainmodel_InterfaceMethodCall getDomainmodel_interfacemethodcall() {
        return domainmodel_interfacemethodcall;
    }

    public void setDomainmodel_interfacemethodcall(domainmodel_InterfaceMethodCall domainmodel_interfacemethodcall) {
        this.domainmodel_interfacemethodcall = domainmodel_interfacemethodcall;
    }
    public domainmodel_BusinessFeature getDomainmodel_businessfeature() {
        return domainmodel_businessfeature;
    }

    public void setDomainmodel_businessfeature(domainmodel_BusinessFeature domainmodel_businessfeature) {
        this.domainmodel_businessfeature = domainmodel_businessfeature;
    }

}