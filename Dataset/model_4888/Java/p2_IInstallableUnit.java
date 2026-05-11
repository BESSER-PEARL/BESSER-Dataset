





import java.util.List;
import java.util.ArrayList;

public class p2_IInstallableUnit  {

    private boolean singleton;
    private boolean resolved;
    private String filter;





    private List<p2_ILicense> p2_ilicenses;




    private p2_ITouchpointType p2_itouchpointtype;




    private List<p2_IRequirement> p2_irequirements;




    private List<p2_ITouchpointData> p2_itouchpointdatas;




    private List<p2_IInstallableUnitFragment> p2_iinstallableunitfragments;




    private List<p2_IRequirement> p2_irequirements;




    private p2_ICopyright p2_icopyright;




    private List<p2_IProvidedCapability> p2_iprovidedcapabilitys;


    public p2_IInstallableUnit(
        boolean singleton,        boolean resolved,        String filter    ) {
        this.singleton = singleton;
        this.resolved = resolved;
        this.filter = filter;
        this.p2_ilicenses = new ArrayList<>();
        this.p2_irequirements = new ArrayList<>();
        this.p2_itouchpointdatas = new ArrayList<>();
        this.p2_iinstallableunitfragments = new ArrayList<>();
        this.p2_irequirements = new ArrayList<>();
        this.p2_iprovidedcapabilitys = new ArrayList<>();
    }

    public p2_IInstallableUnit(
        boolean singleton,        boolean resolved,        String filter        ArrayList<p2_ILicense> p2_ilicenses,        ArrayList<p2_IRequirement> p2_irequirements,        ArrayList<p2_ITouchpointData> p2_itouchpointdatas,        ArrayList<p2_IInstallableUnitFragment> p2_iinstallableunitfragments,        ArrayList<p2_IRequirement> p2_irequirements,        ArrayList<p2_IProvidedCapability> p2_iprovidedcapabilitys    ) {
        this.singleton = singleton;
        this.resolved = resolved;
        this.filter = filter;
        this.p2_ilicenses = p2_ilicenses;
        this.p2_irequirements = p2_irequirements;
        this.p2_itouchpointdatas = p2_itouchpointdatas;
        this.p2_iinstallableunitfragments = p2_iinstallableunitfragments;
        this.p2_irequirements = p2_irequirements;
        this.p2_iprovidedcapabilitys = p2_iprovidedcapabilitys;
    }

    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }

    public List<p2_ILicense> getP2_ilicenses() {
        return p2_ilicenses;
    }

    public void addP2_ilicense(P2_ilicense p2_ilicense) {
        this.p2_ilicenses.add(p2_ilicense);
    }
    public p2_ITouchpointType getP2_itouchpointtype() {
        return p2_itouchpointtype;
    }

    public void setP2_itouchpointtype(p2_ITouchpointType p2_itouchpointtype) {
        this.p2_itouchpointtype = p2_itouchpointtype;
    }
    public List<p2_IRequirement> getP2_irequirements() {
        return p2_irequirements;
    }

    public void addP2_irequirement(P2_irequirement p2_irequirement) {
        this.p2_irequirements.add(p2_irequirement);
    }
    public List<p2_ITouchpointData> getP2_itouchpointdatas() {
        return p2_itouchpointdatas;
    }

    public void addP2_itouchpointdata(P2_itouchpointdata p2_itouchpointdata) {
        this.p2_itouchpointdatas.add(p2_itouchpointdata);
    }
    public List<p2_IInstallableUnitFragment> getP2_iinstallableunitfragments() {
        return p2_iinstallableunitfragments;
    }

    public void addP2_iinstallableunitfragment(P2_iinstallableunitfragment p2_iinstallableunitfragment) {
        this.p2_iinstallableunitfragments.add(p2_iinstallableunitfragment);
    }
    public List<p2_IRequirement> getP2_irequirements() {
        return p2_irequirements;
    }

    public void addP2_irequirement(P2_irequirement p2_irequirement) {
        this.p2_irequirements.add(p2_irequirement);
    }
    public p2_ICopyright getP2_icopyright() {
        return p2_icopyright;
    }

    public void setP2_icopyright(p2_ICopyright p2_icopyright) {
        this.p2_icopyright = p2_icopyright;
    }
    public List<p2_IProvidedCapability> getP2_iprovidedcapabilitys() {
        return p2_iprovidedcapabilitys;
    }

    public void addP2_iprovidedcapability(P2_iprovidedcapability p2_iprovidedcapability) {
        this.p2_iprovidedcapabilitys.add(p2_iprovidedcapability);
    }

}