





import java.util.List;
import java.util.ArrayList;

public class henshin_Unit extends NamedElement {

    private boolean activated;





    private henshin_Module henshin_module;




    private henshin_UnaryUnit henshin_unaryunit;




    private List<henshin_Parameter> henshin_parameters;




    private henshin_ConditionalUnit henshin_conditionalunit;




    private henshin_Parameter henshin_parameter;




    private henshin_ConditionalUnit henshin_conditionalunit;




    private List<henshin_ParameterMapping> henshin_parametermappings;




    private henshin_MultiUnit henshin_multiunit;




    private henshin_ConditionalUnit henshin_conditionalunit;


    public henshin_Unit(
        boolean activated    ) {
        super(
        );
        this.activated = activated;
        this.henshin_parameters = new ArrayList<>();
        this.henshin_parametermappings = new ArrayList<>();
    }

    public henshin_Unit(
        boolean activated        ArrayList<henshin_Parameter> henshin_parameters,        ArrayList<henshin_ParameterMapping> henshin_parametermappings    ) {
        this.activated = activated;
        this.henshin_parameters = henshin_parameters;
        this.henshin_parametermappings = henshin_parametermappings;
    }

    public boolean getActivated() {
        return activated;
    }

    public void setActivated(boolean activated) {
        this.activated = activated;
    }

    public henshin_Module getHenshin_module() {
        return henshin_module;
    }

    public void setHenshin_module(henshin_Module henshin_module) {
        this.henshin_module = henshin_module;
    }
    public henshin_UnaryUnit getHenshin_unaryunit() {
        return henshin_unaryunit;
    }

    public void setHenshin_unaryunit(henshin_UnaryUnit henshin_unaryunit) {
        this.henshin_unaryunit = henshin_unaryunit;
    }
    public List<henshin_Parameter> getHenshin_parameters() {
        return henshin_parameters;
    }

    public void addHenshin_parameter(Henshin_parameter henshin_parameter) {
        this.henshin_parameters.add(henshin_parameter);
    }
    public henshin_ConditionalUnit getHenshin_conditionalunit() {
        return henshin_conditionalunit;
    }

    public void setHenshin_conditionalunit(henshin_ConditionalUnit henshin_conditionalunit) {
        this.henshin_conditionalunit = henshin_conditionalunit;
    }
    public henshin_Parameter getHenshin_parameter() {
        return henshin_parameter;
    }

    public void setHenshin_parameter(henshin_Parameter henshin_parameter) {
        this.henshin_parameter = henshin_parameter;
    }
    public henshin_ConditionalUnit getHenshin_conditionalunit() {
        return henshin_conditionalunit;
    }

    public void setHenshin_conditionalunit(henshin_ConditionalUnit henshin_conditionalunit) {
        this.henshin_conditionalunit = henshin_conditionalunit;
    }
    public List<henshin_ParameterMapping> getHenshin_parametermappings() {
        return henshin_parametermappings;
    }

    public void addHenshin_parametermapping(Henshin_parametermapping henshin_parametermapping) {
        this.henshin_parametermappings.add(henshin_parametermapping);
    }
    public henshin_MultiUnit getHenshin_multiunit() {
        return henshin_multiunit;
    }

    public void setHenshin_multiunit(henshin_MultiUnit henshin_multiunit) {
        this.henshin_multiunit = henshin_multiunit;
    }
    public henshin_ConditionalUnit getHenshin_conditionalunit() {
        return henshin_conditionalunit;
    }

    public void setHenshin_conditionalunit(henshin_ConditionalUnit henshin_conditionalunit) {
        this.henshin_conditionalunit = henshin_conditionalunit;
    }

}