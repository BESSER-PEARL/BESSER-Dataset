





import java.util.List;
import java.util.ArrayList;

public class docbook_Link extends ParaMixedContent {






    private docbook_ParaMixedContent docbook_paramixedcontent;




    private List<docbook_ParaMixedContent> docbook_paramixedcontents;


    public docbook_Link(
    ) {
        super(
        );
        this.docbook_paramixedcontents = new ArrayList<>();
    }

    public docbook_Link(
        ArrayList<docbook_ParaMixedContent> docbook_paramixedcontents    ) {
        this.docbook_paramixedcontents = docbook_paramixedcontents;
    }


    public docbook_ParaMixedContent getDocbook_paramixedcontent() {
        return docbook_paramixedcontent;
    }

    public void setDocbook_paramixedcontent(docbook_ParaMixedContent docbook_paramixedcontent) {
        this.docbook_paramixedcontent = docbook_paramixedcontent;
    }
    public List<docbook_ParaMixedContent> getDocbook_paramixedcontents() {
        return docbook_paramixedcontents;
    }

    public void addDocbook_paramixedcontent(Docbook_paramixedcontent docbook_paramixedcontent) {
        this.docbook_paramixedcontents.add(docbook_paramixedcontent);
    }

}