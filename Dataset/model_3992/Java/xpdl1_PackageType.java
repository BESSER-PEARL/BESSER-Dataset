





import java.util.List;
import java.util.ArrayList;

public class xpdl1_PackageType  {

    private String id;
    private String name;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;




    private xpdl1_ApplicationsType xpdl1_applicationstype;




    private xpdl1_DataFieldsType xpdl1_datafieldstype;




    private xpdl1_ConformanceClassType xpdl1_conformanceclasstype;




    private xpdl1_ExternalPackagesType xpdl1_externalpackagestype;


    public xpdl1_PackageType(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }
    public xpdl1_ApplicationsType getXpdl1_applicationstype() {
        return xpdl1_applicationstype;
    }

    public void setXpdl1_applicationstype(xpdl1_ApplicationsType xpdl1_applicationstype) {
        this.xpdl1_applicationstype = xpdl1_applicationstype;
    }
    public xpdl1_DataFieldsType getXpdl1_datafieldstype() {
        return xpdl1_datafieldstype;
    }

    public void setXpdl1_datafieldstype(xpdl1_DataFieldsType xpdl1_datafieldstype) {
        this.xpdl1_datafieldstype = xpdl1_datafieldstype;
    }
    public xpdl1_ConformanceClassType getXpdl1_conformanceclasstype() {
        return xpdl1_conformanceclasstype;
    }

    public void setXpdl1_conformanceclasstype(xpdl1_ConformanceClassType xpdl1_conformanceclasstype) {
        this.xpdl1_conformanceclasstype = xpdl1_conformanceclasstype;
    }
    public xpdl1_ExternalPackagesType getXpdl1_externalpackagestype() {
        return xpdl1_externalpackagestype;
    }

    public void setXpdl1_externalpackagestype(xpdl1_ExternalPackagesType xpdl1_externalpackagestype) {
        this.xpdl1_externalpackagestype = xpdl1_externalpackagestype;
    }

}