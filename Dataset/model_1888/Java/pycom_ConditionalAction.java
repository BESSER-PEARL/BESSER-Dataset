





import java.util.List;
import java.util.ArrayList;

public class pycom_ConditionalAction extends ExpMember {

    private String type;





    private List<pycom_ExpMember> pycom_expmembers;




    private pycom_Server pycom_server;


    public pycom_ConditionalAction(
        String type    ) {
        super(
        );
        this.type = type;
        this.pycom_expmembers = new ArrayList<>();
    }

    public pycom_ConditionalAction(
        String type        ArrayList<pycom_ExpMember> pycom_expmembers    ) {
        this.type = type;
        this.pycom_expmembers = pycom_expmembers;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<pycom_ExpMember> getPycom_expmembers() {
        return pycom_expmembers;
    }

    public void addPycom_expmember(Pycom_expmember pycom_expmember) {
        this.pycom_expmembers.add(pycom_expmember);
    }
    public pycom_Server getPycom_server() {
        return pycom_server;
    }

    public void setPycom_server(pycom_Server pycom_server) {
        this.pycom_server = pycom_server;
    }

}