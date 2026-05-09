





import java.util.List;
import java.util.ArrayList;

public class domain_Operation extends Categorized, Secured {

    private String name;
    private String uid;





    private domain_Parameter domain_parameter;




    private List<domain_Parameter> domain_parameters;




    private domain_MethodPointer domain_methodpointer;




    private domain_ReturnValue domain_returnvalue;


    public domain_Operation(
        String name,        String uid    ) {
        super(
        );
        this.name = name;
        this.uid = uid;
        this.domain_parameters = new ArrayList<>();
    }

    public domain_Operation(
        String name,        String uid        ArrayList<domain_Parameter> domain_parameters    ) {
        this.name = name;
        this.uid = uid;
        this.domain_parameters = domain_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Parameter getDomain_parameter() {
        return domain_parameter;
    }

    public void setDomain_parameter(domain_Parameter domain_parameter) {
        this.domain_parameter = domain_parameter;
    }
    public List<domain_Parameter> getDomain_parameters() {
        return domain_parameters;
    }

    public void addDomain_parameter(Domain_parameter domain_parameter) {
        this.domain_parameters.add(domain_parameter);
    }
    public domain_MethodPointer getDomain_methodpointer() {
        return domain_methodpointer;
    }

    public void setDomain_methodpointer(domain_MethodPointer domain_methodpointer) {
        this.domain_methodpointer = domain_methodpointer;
    }
    public domain_ReturnValue getDomain_returnvalue() {
        return domain_returnvalue;
    }

    public void setDomain_returnvalue(domain_ReturnValue domain_returnvalue) {
        this.domain_returnvalue = domain_returnvalue;
    }

}