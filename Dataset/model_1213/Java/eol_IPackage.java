





import java.util.List;
import java.util.ArrayList;

public class eol_IPackage extends EOLElement {

    private String name;
    private String iPackageDriver;
    private String nsPrefix;





    private eol_IPackage eol_ipackage;




    private eol_IModel eol_imodel;


    public eol_IPackage(
        String name,        String iPackageDriver,        String nsPrefix    ) {
        super(
        );
        this.name = name;
        this.iPackageDriver = iPackageDriver;
        this.nsPrefix = nsPrefix;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIpackagedriver() {
        return iPackageDriver;
    }

    public void setIpackagedriver(String iPackageDriver) {
        this.iPackageDriver = iPackageDriver;
    }
    public String getNsprefix() {
        return nsPrefix;
    }

    public void setNsprefix(String nsPrefix) {
        this.nsPrefix = nsPrefix;
    }

    public eol_IPackage getEol_ipackage() {
        return eol_ipackage;
    }

    public void setEol_ipackage(eol_IPackage eol_ipackage) {
        this.eol_ipackage = eol_ipackage;
    }
    public eol_IModel getEol_imodel() {
        return eol_imodel;
    }

    public void setEol_imodel(eol_IModel eol_imodel) {
        this.eol_imodel = eol_imodel;
    }

}