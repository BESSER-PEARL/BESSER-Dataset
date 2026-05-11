





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_Connector extends DomainModelPort {

    private String Class;
    private String Locator;





    private List<Parameter> parameters;




    private List<Redeclare> redeclares;


    public avm_modelica_Connector(
        String Class,        String Locator    ) {
        super(
        );
        this.Class = Class;
        this.Locator = Locator;
        this.parameters = new ArrayList<>();
        this.redeclares = new ArrayList<>();
    }

    public avm_modelica_Connector(
        String Class,        String Locator        ArrayList<Parameter> parameters,        ArrayList<Redeclare> redeclares    ) {
        this.Class = Class;
        this.Locator = Locator;
        this.parameters = parameters;
        this.redeclares = redeclares;
    }

    public String getClass() {
        return Class;
    }

    public void setClass(String Class) {
        this.Class = Class;
    }
    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }

    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }
    public List<Redeclare> getRedeclares() {
        return redeclares;
    }

    public void addRedeclare(Redeclare redeclare) {
        this.redeclares.add(redeclare);
    }

}