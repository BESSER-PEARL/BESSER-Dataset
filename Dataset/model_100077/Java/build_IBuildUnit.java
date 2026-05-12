





import java.util.List;
import java.util.ArrayList;

public class build_IBuildUnit extends IGenericUnit, PropertyScope, ICapability {

    private boolean circularityAllowed;
    private String filter;
    private String instanceLocation;





    private List<build_IRequiredCapability> build_irequiredcapabilitys;




    private List<build_IRequiredCapability> build_irequiredcapabilitys;




    private build_IBuildUnit build_ibuildunit;




    private List<build_ICapability> build_icapabilitys;




    private List<build_IRequiredCapability> build_irequiredcapabilitys;




    private build_IBuildPart build_ibuildpart;




    private List<build_IBuildPart> build_ibuildparts;


    public build_IBuildUnit(
        boolean circularityAllowed,        String filter,        String instanceLocation    ) {
        super(
        );
        this.circularityAllowed = circularityAllowed;
        this.filter = filter;
        this.instanceLocation = instanceLocation;
        this.build_irequiredcapabilitys = new ArrayList<>();
        this.build_irequiredcapabilitys = new ArrayList<>();
        this.build_icapabilitys = new ArrayList<>();
        this.build_irequiredcapabilitys = new ArrayList<>();
        this.build_ibuildparts = new ArrayList<>();
    }

    public build_IBuildUnit(
        boolean circularityAllowed,        String filter,        String instanceLocation        ArrayList<build_IRequiredCapability> build_irequiredcapabilitys,        ArrayList<build_IRequiredCapability> build_irequiredcapabilitys,        ArrayList<build_ICapability> build_icapabilitys,        ArrayList<build_IRequiredCapability> build_irequiredcapabilitys,        ArrayList<build_IBuildPart> build_ibuildparts    ) {
        this.circularityAllowed = circularityAllowed;
        this.filter = filter;
        this.instanceLocation = instanceLocation;
        this.build_irequiredcapabilitys = build_irequiredcapabilitys;
        this.build_irequiredcapabilitys = build_irequiredcapabilitys;
        this.build_icapabilitys = build_icapabilitys;
        this.build_irequiredcapabilitys = build_irequiredcapabilitys;
        this.build_ibuildparts = build_ibuildparts;
    }

    public boolean getCircularityallowed() {
        return circularityAllowed;
    }

    public void setCircularityallowed(boolean circularityAllowed) {
        this.circularityAllowed = circularityAllowed;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getInstancelocation() {
        return instanceLocation;
    }

    public void setInstancelocation(String instanceLocation) {
        this.instanceLocation = instanceLocation;
    }

    public List<build_IRequiredCapability> getBuild_irequiredcapabilitys() {
        return build_irequiredcapabilitys;
    }

    public void addBuild_irequiredcapability(Build_irequiredcapability build_irequiredcapability) {
        this.build_irequiredcapabilitys.add(build_irequiredcapability);
    }
    public List<build_IRequiredCapability> getBuild_irequiredcapabilitys() {
        return build_irequiredcapabilitys;
    }

    public void addBuild_irequiredcapability(Build_irequiredcapability build_irequiredcapability) {
        this.build_irequiredcapabilitys.add(build_irequiredcapability);
    }
    public build_IBuildUnit getBuild_ibuildunit() {
        return build_ibuildunit;
    }

    public void setBuild_ibuildunit(build_IBuildUnit build_ibuildunit) {
        this.build_ibuildunit = build_ibuildunit;
    }
    public List<build_ICapability> getBuild_icapabilitys() {
        return build_icapabilitys;
    }

    public void addBuild_icapability(Build_icapability build_icapability) {
        this.build_icapabilitys.add(build_icapability);
    }
    public List<build_IRequiredCapability> getBuild_irequiredcapabilitys() {
        return build_irequiredcapabilitys;
    }

    public void addBuild_irequiredcapability(Build_irequiredcapability build_irequiredcapability) {
        this.build_irequiredcapabilitys.add(build_irequiredcapability);
    }
    public build_IBuildPart getBuild_ibuildpart() {
        return build_ibuildpart;
    }

    public void setBuild_ibuildpart(build_IBuildPart build_ibuildpart) {
        this.build_ibuildpart = build_ibuildpart;
    }
    public List<build_IBuildPart> getBuild_ibuildparts() {
        return build_ibuildparts;
    }

    public void addBuild_ibuildpart(Build_ibuildpart build_ibuildpart) {
        this.build_ibuildparts.add(build_ibuildpart);
    }

}