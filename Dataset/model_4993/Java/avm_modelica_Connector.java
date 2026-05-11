





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_Connector extends DomainModelPort {

    private String Class;
    private String Locator;





    private List<Redeclare> redeclares;




    private List<Parameter> parameters;


    public avm_modelica_Connector(
        String Class,        String Locator    ) {
        super(
        );
        this.Class = Class;
        this.Locator = Locator;
        this.redeclares = new ArrayList<>();
        this.parameters = new ArrayList<>();
    }

    public avm_modelica_Connector(
        String Class,        String Locator        ArrayList<Redeclare> redeclares,        ArrayList<Parameter> parameters    ) {
        this.Class = Class;
        this.Locator = Locator;
        this.redeclares = redeclares;
        this.parameters = parameters;
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

    public List<Redeclare> getRedeclares() {
        return redeclares;
    }

    public void addRedeclare(Redeclare redeclare) {
        this.redeclares.add(redeclare);
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}