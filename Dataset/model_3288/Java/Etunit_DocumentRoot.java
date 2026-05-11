





import java.util.List;
import java.util.ArrayList;

public class Etunit_DocumentRoot  {

    private String systemOut;
    private String mixed;
    private String systemErr;





    private List<Etunit_ErrorType> etunit_errortypes;




    private List<Etunit_PropertiesType> etunit_propertiestypes;




    private List<Etunit_FailureType> etunit_failuretypes;


    public Etunit_DocumentRoot(
        String systemOut,        String mixed,        String systemErr    ) {
        this.systemOut = systemOut;
        this.mixed = mixed;
        this.systemErr = systemErr;
        this.etunit_errortypes = new ArrayList<>();
        this.etunit_propertiestypes = new ArrayList<>();
        this.etunit_failuretypes = new ArrayList<>();
    }

    public Etunit_DocumentRoot(
        String systemOut,        String mixed,        String systemErr        ArrayList<Etunit_ErrorType> etunit_errortypes,        ArrayList<Etunit_PropertiesType> etunit_propertiestypes,        ArrayList<Etunit_FailureType> etunit_failuretypes    ) {
        this.systemOut = systemOut;
        this.mixed = mixed;
        this.systemErr = systemErr;
        this.etunit_errortypes = etunit_errortypes;
        this.etunit_propertiestypes = etunit_propertiestypes;
        this.etunit_failuretypes = etunit_failuretypes;
    }

    public String getSystemout() {
        return systemOut;
    }

    public void setSystemout(String systemOut) {
        this.systemOut = systemOut;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getSystemerr() {
        return systemErr;
    }

    public void setSystemerr(String systemErr) {
        this.systemErr = systemErr;
    }

    public List<Etunit_ErrorType> getEtunit_errortypes() {
        return etunit_errortypes;
    }

    public void addEtunit_errortype(Etunit_errortype etunit_errortype) {
        this.etunit_errortypes.add(etunit_errortype);
    }
    public List<Etunit_PropertiesType> getEtunit_propertiestypes() {
        return etunit_propertiestypes;
    }

    public void addEtunit_propertiestype(Etunit_propertiestype etunit_propertiestype) {
        this.etunit_propertiestypes.add(etunit_propertiestype);
    }
    public List<Etunit_FailureType> getEtunit_failuretypes() {
        return etunit_failuretypes;
    }

    public void addEtunit_failuretype(Etunit_failuretype etunit_failuretype) {
        this.etunit_failuretypes.add(etunit_failuretype);
    }

}