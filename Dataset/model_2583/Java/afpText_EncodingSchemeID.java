





import java.util.List;
import java.util.ArrayList;

public class afpText_EncodingSchemeID extends triplet {

    private String ESidUD;
    private String ESidCP;



    public afpText_EncodingSchemeID(
        String ESidUD,        String ESidCP    ) {
        super(
        );
        this.ESidUD = ESidUD;
        this.ESidCP = ESidCP;
    }


    public String getEsidud() {
        return ESidUD;
    }

    public void setEsidud(String ESidUD) {
        this.ESidUD = ESidUD;
    }
    public String getEsidcp() {
        return ESidCP;
    }

    public void setEsidcp(String ESidCP) {
        this.ESidCP = ESidCP;
    }


}