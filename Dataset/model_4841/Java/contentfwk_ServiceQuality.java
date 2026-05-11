





import java.util.List;
import java.util.ArrayList;

public class contentfwk_ServiceQuality extends Element {






    private contentfwk_Contract contentfwk_contract;




    private List<contentfwk_Contract> contentfwk_contracts;


    public contentfwk_ServiceQuality(
    ) {
        super(
        );
        this.contentfwk_contracts = new ArrayList<>();
    }

    public contentfwk_ServiceQuality(
        ArrayList<contentfwk_Contract> contentfwk_contracts    ) {
        this.contentfwk_contracts = contentfwk_contracts;
    }


    public contentfwk_Contract getContentfwk_contract() {
        return contentfwk_contract;
    }

    public void setContentfwk_contract(contentfwk_Contract contentfwk_contract) {
        this.contentfwk_contract = contentfwk_contract;
    }
    public List<contentfwk_Contract> getContentfwk_contracts() {
        return contentfwk_contracts;
    }

    public void addContentfwk_contract(Contentfwk_contract contentfwk_contract) {
        this.contentfwk_contracts.add(contentfwk_contract);
    }

}