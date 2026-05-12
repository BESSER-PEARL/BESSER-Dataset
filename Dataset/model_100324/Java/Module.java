





import java.util.List;
import java.util.ArrayList;

public class Module  {






    private PNML_Interface pnml_interface;




    private PNML_PNMLDocument pnml_pnmldocument;


    public Module(
    ) {
    }



    public PNML_Interface getPnml_interface() {
        return pnml_interface;
    }

    public void setPnml_interface(PNML_Interface pnml_interface) {
        this.pnml_interface = pnml_interface;
    }
    public PNML_PNMLDocument getPnml_pnmldocument() {
        return pnml_pnmldocument;
    }

    public void setPnml_pnmldocument(PNML_PNMLDocument pnml_pnmldocument) {
        this.pnml_pnmldocument = pnml_pnmldocument;
    }

}