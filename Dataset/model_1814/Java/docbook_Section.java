





import java.util.List;
import java.util.ArrayList;

public class docbook_Section extends TitledElement {






    private List<docbook_Para> docbook_paras;


    public docbook_Section(
    ) {
        super(
        );
        this.docbook_paras = new ArrayList<>();
    }

    public docbook_Section(
        ArrayList<docbook_Para> docbook_paras    ) {
        this.docbook_paras = docbook_paras;
    }


    public List<docbook_Para> getDocbook_paras() {
        return docbook_paras;
    }

    public void addDocbook_para(Docbook_para docbook_para) {
        this.docbook_paras.add(docbook_para);
    }

}