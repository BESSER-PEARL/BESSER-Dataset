





import java.util.List;
import java.util.ArrayList;

public class docbook_Emphasis extends ParaMixedContent {






    private List<docbook_ParaMixedContent> docbook_paramixedcontents;




    private docbook_ParaMixedContent docbook_paramixedcontent;


    public docbook_Emphasis(
    ) {
        super(
        );
        this.docbook_paramixedcontents = new ArrayList<>();
    }

    public docbook_Emphasis(
        ArrayList<docbook_ParaMixedContent> docbook_paramixedcontents    ) {
        this.docbook_paramixedcontents = docbook_paramixedcontents;
    }


    public List<docbook_ParaMixedContent> getDocbook_paramixedcontents() {
        return docbook_paramixedcontents;
    }

    public void addDocbook_paramixedcontent(Docbook_paramixedcontent docbook_paramixedcontent) {
        this.docbook_paramixedcontents.add(docbook_paramixedcontent);
    }
    public docbook_ParaMixedContent getDocbook_paramixedcontent() {
        return docbook_paramixedcontent;
    }

    public void setDocbook_paramixedcontent(docbook_ParaMixedContent docbook_paramixedcontent) {
        this.docbook_paramixedcontent = docbook_paramixedcontent;
    }

}