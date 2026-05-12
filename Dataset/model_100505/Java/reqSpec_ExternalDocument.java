





import java.util.List;
import java.util.ArrayList;

public class reqSpec_ExternalDocument  {

    private String docFragment;
    private String docReference;





    private reqSpec_ContractualElement reqspec_contractualelement;


    public reqSpec_ExternalDocument(
        String docFragment,        String docReference    ) {
        this.docFragment = docFragment;
        this.docReference = docReference;
    }


    public String getDocfragment() {
        return docFragment;
    }

    public void setDocfragment(String docFragment) {
        this.docFragment = docFragment;
    }
    public String getDocreference() {
        return docReference;
    }

    public void setDocreference(String docReference) {
        this.docReference = docReference;
    }

    public reqSpec_ContractualElement getReqspec_contractualelement() {
        return reqspec_contractualelement;
    }

    public void setReqspec_contractualelement(reqSpec_ContractualElement reqspec_contractualelement) {
        this.reqspec_contractualelement = reqspec_contractualelement;
    }

}