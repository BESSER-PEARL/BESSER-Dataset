





import java.util.List;
import java.util.ArrayList;

public class iso20022_Participant extends MultiplicityEntity, RepositoryConcept {






    private List<iso20022_Receive> iso20022_receives;




    private iso20022_BusinessTransaction iso20022_businesstransaction;




    private iso20022_BusinessTransaction iso20022_businesstransaction;




    private iso20022_Receive iso20022_receive;




    private iso20022_Send iso20022_send;




    private List<iso20022_Send> iso20022_sends;


    public iso20022_Participant(
    ) {
        super(
        );
        this.iso20022_receives = new ArrayList<>();
        this.iso20022_sends = new ArrayList<>();
    }

    public iso20022_Participant(
        ArrayList<iso20022_Receive> iso20022_receives,        ArrayList<iso20022_Send> iso20022_sends    ) {
        this.iso20022_receives = iso20022_receives;
        this.iso20022_sends = iso20022_sends;
    }


    public List<iso20022_Receive> getIso20022_receives() {
        return iso20022_receives;
    }

    public void addIso20022_receive(Iso20022_receive iso20022_receive) {
        this.iso20022_receives.add(iso20022_receive);
    }
    public iso20022_BusinessTransaction getIso20022_businesstransaction() {
        return iso20022_businesstransaction;
    }

    public void setIso20022_businesstransaction(iso20022_BusinessTransaction iso20022_businesstransaction) {
        this.iso20022_businesstransaction = iso20022_businesstransaction;
    }
    public iso20022_BusinessTransaction getIso20022_businesstransaction() {
        return iso20022_businesstransaction;
    }

    public void setIso20022_businesstransaction(iso20022_BusinessTransaction iso20022_businesstransaction) {
        this.iso20022_businesstransaction = iso20022_businesstransaction;
    }
    public iso20022_Receive getIso20022_receive() {
        return iso20022_receive;
    }

    public void setIso20022_receive(iso20022_Receive iso20022_receive) {
        this.iso20022_receive = iso20022_receive;
    }
    public iso20022_Send getIso20022_send() {
        return iso20022_send;
    }

    public void setIso20022_send(iso20022_Send iso20022_send) {
        this.iso20022_send = iso20022_send;
    }
    public List<iso20022_Send> getIso20022_sends() {
        return iso20022_sends;
    }

    public void addIso20022_send(Iso20022_send iso20022_send) {
        this.iso20022_sends.add(iso20022_send);
    }

}