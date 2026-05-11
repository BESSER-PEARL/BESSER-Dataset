





import java.util.List;
import java.util.ArrayList;

public class model_PartnerLinks extends BPELExtensibleElement {






    private List<model_PartnerLink> model_partnerlinks;




    private model_Process model_process;


    public model_PartnerLinks(
    ) {
        super(
        );
        this.model_partnerlinks = new ArrayList<>();
    }

    public model_PartnerLinks(
        ArrayList<model_PartnerLink> model_partnerlinks    ) {
        this.model_partnerlinks = model_partnerlinks;
    }


    public List<model_PartnerLink> getModel_partnerlinks() {
        return model_partnerlinks;
    }

    public void addModel_partnerlink(Model_partnerlink model_partnerlink) {
        this.model_partnerlinks.add(model_partnerlink);
    }
    public model_Process getModel_process() {
        return model_process;
    }

    public void setModel_process(model_Process model_process) {
        this.model_process = model_process;
    }

}