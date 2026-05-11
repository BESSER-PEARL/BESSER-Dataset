





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Method  {

    private String Name;
    private String Body;





    private ORDB4ORA_StructuredType ordb4ora_structuredtype;




    private ORDB4ORA_Datatype ordb4ora_datatype;




    private ORDB4ORA_MethodParameter ordb4ora_methodparameter;




    private ORDB4ORA_StructuredType ordb4ora_structuredtype;




    private ORDB4ORA_Method ordb4ora_method;




    private List<ORDB4ORA_MethodParameter> ordb4ora_methodparameters;


    public ORDB4ORA_Method(
        String Name,        String Body    ) {
        this.Name = Name;
        this.Body = Body;
        this.ordb4ora_methodparameters = new ArrayList<>();
    }

    public ORDB4ORA_Method(
        String Name,        String Body        ArrayList<ORDB4ORA_MethodParameter> ordb4ora_methodparameters    ) {
        this.Name = Name;
        this.Body = Body;
        this.ordb4ora_methodparameters = ordb4ora_methodparameters;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }

    public ORDB4ORA_StructuredType getOrdb4ora_structuredtype() {
        return ordb4ora_structuredtype;
    }

    public void setOrdb4ora_structuredtype(ORDB4ORA_StructuredType ordb4ora_structuredtype) {
        this.ordb4ora_structuredtype = ordb4ora_structuredtype;
    }
    public ORDB4ORA_Datatype getOrdb4ora_datatype() {
        return ordb4ora_datatype;
    }

    public void setOrdb4ora_datatype(ORDB4ORA_Datatype ordb4ora_datatype) {
        this.ordb4ora_datatype = ordb4ora_datatype;
    }
    public ORDB4ORA_MethodParameter getOrdb4ora_methodparameter() {
        return ordb4ora_methodparameter;
    }

    public void setOrdb4ora_methodparameter(ORDB4ORA_MethodParameter ordb4ora_methodparameter) {
        this.ordb4ora_methodparameter = ordb4ora_methodparameter;
    }
    public ORDB4ORA_StructuredType getOrdb4ora_structuredtype() {
        return ordb4ora_structuredtype;
    }

    public void setOrdb4ora_structuredtype(ORDB4ORA_StructuredType ordb4ora_structuredtype) {
        this.ordb4ora_structuredtype = ordb4ora_structuredtype;
    }
    public ORDB4ORA_Method getOrdb4ora_method() {
        return ordb4ora_method;
    }

    public void setOrdb4ora_method(ORDB4ORA_Method ordb4ora_method) {
        this.ordb4ora_method = ordb4ora_method;
    }
    public List<ORDB4ORA_MethodParameter> getOrdb4ora_methodparameters() {
        return ordb4ora_methodparameters;
    }

    public void addOrdb4ora_methodparameter(Ordb4ora_methodparameter ordb4ora_methodparameter) {
        this.ordb4ora_methodparameters.add(ordb4ora_methodparameter);
    }

}