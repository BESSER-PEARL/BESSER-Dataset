





import java.util.List;
import java.util.ArrayList;

public class alf_InstanceCreationTupleElement  {

    private String role;





    private alf_InstanceCreationTuple alf_instancecreationtuple;




    private alf_Expression alf_expression;


    public alf_InstanceCreationTupleElement(
        String role    ) {
        this.role = role;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public alf_InstanceCreationTuple getAlf_instancecreationtuple() {
        return alf_instancecreationtuple;
    }

    public void setAlf_instancecreationtuple(alf_InstanceCreationTuple alf_instancecreationtuple) {
        this.alf_instancecreationtuple = alf_instancecreationtuple;
    }
    public alf_Expression getAlf_expression() {
        return alf_expression;
    }

    public void setAlf_expression(alf_Expression alf_expression) {
        this.alf_expression = alf_expression;
    }

}