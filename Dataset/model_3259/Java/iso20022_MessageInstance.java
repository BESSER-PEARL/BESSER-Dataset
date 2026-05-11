





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageInstance extends ModelEntity {






    private List<iso20022_TransportMessage> iso20022_transportmessages;




    private iso20022_TransportMessage iso20022_transportmessage;


    public iso20022_MessageInstance(
    ) {
        super(
        );
        this.iso20022_transportmessages = new ArrayList<>();
    }

    public iso20022_MessageInstance(
        ArrayList<iso20022_TransportMessage> iso20022_transportmessages    ) {
        this.iso20022_transportmessages = iso20022_transportmessages;
    }


    public List<iso20022_TransportMessage> getIso20022_transportmessages() {
        return iso20022_transportmessages;
    }

    public void addIso20022_transportmessage(Iso20022_transportmessage iso20022_transportmessage) {
        this.iso20022_transportmessages.add(iso20022_transportmessage);
    }
    public iso20022_TransportMessage getIso20022_transportmessage() {
        return iso20022_transportmessage;
    }

    public void setIso20022_transportmessage(iso20022_TransportMessage iso20022_transportmessage) {
        this.iso20022_transportmessage = iso20022_transportmessage;
    }

}