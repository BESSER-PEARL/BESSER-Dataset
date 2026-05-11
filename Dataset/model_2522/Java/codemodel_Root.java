





import java.util.List;
import java.util.ArrayList;

public class codemodel_Root extends CMElement {






    private List<codemodel_CMElement> codemodel_cmelements;


    public codemodel_Root(
    ) {
        super(
        );
        this.codemodel_cmelements = new ArrayList<>();
    }

    public codemodel_Root(
        ArrayList<codemodel_CMElement> codemodel_cmelements    ) {
        this.codemodel_cmelements = codemodel_cmelements;
    }


    public List<codemodel_CMElement> getCodemodel_cmelements() {
        return codemodel_cmelements;
    }

    public void addCodemodel_cmelement(Codemodel_cmelement codemodel_cmelement) {
        this.codemodel_cmelements.add(codemodel_cmelement);
    }

}