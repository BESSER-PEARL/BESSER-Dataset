





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Operation  {

    private String Body;
    private String Name;





    private ORDB4ORA_OperationParameter ordb4ora_operationparameter;




    private ORDB4ORA_Model ordb4ora_model;




    private ORDB4ORA_Model ordb4ora_model;




    private List<ORDB4ORA_OperationParameter> ordb4ora_operationparameters;


    public ORDB4ORA_Operation(
        String Body,        String Name    ) {
        this.Body = Body;
        this.Name = Name;
        this.ordb4ora_operationparameters = new ArrayList<>();
    }

    public ORDB4ORA_Operation(
        String Body,        String Name        ArrayList<ORDB4ORA_OperationParameter> ordb4ora_operationparameters    ) {
        this.Body = Body;
        this.Name = Name;
        this.ordb4ora_operationparameters = ordb4ora_operationparameters;
    }

    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public ORDB4ORA_OperationParameter getOrdb4ora_operationparameter() {
        return ordb4ora_operationparameter;
    }

    public void setOrdb4ora_operationparameter(ORDB4ORA_OperationParameter ordb4ora_operationparameter) {
        this.ordb4ora_operationparameter = ordb4ora_operationparameter;
    }
    public ORDB4ORA_Model getOrdb4ora_model() {
        return ordb4ora_model;
    }

    public void setOrdb4ora_model(ORDB4ORA_Model ordb4ora_model) {
        this.ordb4ora_model = ordb4ora_model;
    }
    public ORDB4ORA_Model getOrdb4ora_model() {
        return ordb4ora_model;
    }

    public void setOrdb4ora_model(ORDB4ORA_Model ordb4ora_model) {
        this.ordb4ora_model = ordb4ora_model;
    }
    public List<ORDB4ORA_OperationParameter> getOrdb4ora_operationparameters() {
        return ordb4ora_operationparameters;
    }

    public void addOrdb4ora_operationparameter(Ordb4ora_operationparameter ordb4ora_operationparameter) {
        this.ordb4ora_operationparameters.add(ordb4ora_operationparameter);
    }

}