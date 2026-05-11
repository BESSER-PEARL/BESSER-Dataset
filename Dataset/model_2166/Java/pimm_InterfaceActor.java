





import java.util.List;
import java.util.ArrayList;

public class pimm_InterfaceActor extends AbstractActor {

    private String kind;



    public pimm_InterfaceActor(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}