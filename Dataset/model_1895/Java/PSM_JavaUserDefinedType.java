





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaUserDefinedType extends JavaDataType {






    private List<PSM_JavaMethod> psm_javamethods;




    private PSM_JavaUserDefinedType psm_javauserdefinedtype;




    private PSM_JavaMethod psm_javamethod;




    private List<PSM_JavaDataField> psm_javadatafields;




    private PSM_JavaUserDefinedType psm_javauserdefinedtype;




    private PSM_SpringWebApplicationLayer psm_springwebapplicationlayer;




    private PSM_JavaUserDefinedType psm_javauserdefinedtype;


    public PSM_JavaUserDefinedType(
    ) {
        super(
        );
        this.psm_javamethods = new ArrayList<>();
        this.psm_javadatafields = new ArrayList<>();
    }

    public PSM_JavaUserDefinedType(
        ArrayList<PSM_JavaMethod> psm_javamethods,        ArrayList<PSM_JavaDataField> psm_javadatafields    ) {
        this.psm_javamethods = psm_javamethods;
        this.psm_javadatafields = psm_javadatafields;
    }


    public List<PSM_JavaMethod> getPsm_javamethods() {
        return psm_javamethods;
    }

    public void addPsm_javamethod(Psm_javamethod psm_javamethod) {
        this.psm_javamethods.add(psm_javamethod);
    }
    public PSM_JavaUserDefinedType getPsm_javauserdefinedtype() {
        return psm_javauserdefinedtype;
    }

    public void setPsm_javauserdefinedtype(PSM_JavaUserDefinedType psm_javauserdefinedtype) {
        this.psm_javauserdefinedtype = psm_javauserdefinedtype;
    }
    public PSM_JavaMethod getPsm_javamethod() {
        return psm_javamethod;
    }

    public void setPsm_javamethod(PSM_JavaMethod psm_javamethod) {
        this.psm_javamethod = psm_javamethod;
    }
    public List<PSM_JavaDataField> getPsm_javadatafields() {
        return psm_javadatafields;
    }

    public void addPsm_javadatafield(Psm_javadatafield psm_javadatafield) {
        this.psm_javadatafields.add(psm_javadatafield);
    }
    public PSM_JavaUserDefinedType getPsm_javauserdefinedtype() {
        return psm_javauserdefinedtype;
    }

    public void setPsm_javauserdefinedtype(PSM_JavaUserDefinedType psm_javauserdefinedtype) {
        this.psm_javauserdefinedtype = psm_javauserdefinedtype;
    }
    public PSM_SpringWebApplicationLayer getPsm_springwebapplicationlayer() {
        return psm_springwebapplicationlayer;
    }

    public void setPsm_springwebapplicationlayer(PSM_SpringWebApplicationLayer psm_springwebapplicationlayer) {
        this.psm_springwebapplicationlayer = psm_springwebapplicationlayer;
    }
    public PSM_JavaUserDefinedType getPsm_javauserdefinedtype() {
        return psm_javauserdefinedtype;
    }

    public void setPsm_javauserdefinedtype(PSM_JavaUserDefinedType psm_javauserdefinedtype) {
        this.psm_javauserdefinedtype = psm_javauserdefinedtype;
    }

}