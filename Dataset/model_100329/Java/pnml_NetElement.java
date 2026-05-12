





import java.util.List;
import java.util.ArrayList;

public class pnml_NetElement extends Element {

    private String name;





    private pnml_PNMLDocument pnml_pnmldocument;


    public pnml_NetElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pnml_PNMLDocument getPnml_pnmldocument() {
        return pnml_pnmldocument;
    }

    public void setPnml_pnmldocument(pnml_PNMLDocument pnml_pnmldocument) {
        this.pnml_pnmldocument = pnml_pnmldocument;
    }

}