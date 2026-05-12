





import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Message  {

    private String Id;
    private String Value;





    private Covoiturage_Passager covoiturage_passager;


    public Covoiturage_Message(
        String Id,        String Value    ) {
        this.Id = Id;
        this.Value = Value;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }

    public Covoiturage_Passager getCovoiturage_passager() {
        return covoiturage_passager;
    }

    public void setCovoiturage_passager(Covoiturage_Passager covoiturage_passager) {
        this.covoiturage_passager = covoiturage_passager;
    }

}