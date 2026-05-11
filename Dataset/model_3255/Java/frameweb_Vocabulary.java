





import java.util.List;
import java.util.ArrayList;

public class frameweb_Vocabulary extends Package {

    private String vocabularyDocument;





    private List<frameweb_Axiom> frameweb_axioms;




    private frameweb_IRI frameweb_iri;




    private List<frameweb_Annotation> frameweb_annotations;




    private List<frameweb_IRI> frameweb_iris;


    public frameweb_Vocabulary(
        String vocabularyDocument    ) {
        super(
        );
        this.vocabularyDocument = vocabularyDocument;
        this.frameweb_axioms = new ArrayList<>();
        this.frameweb_annotations = new ArrayList<>();
        this.frameweb_iris = new ArrayList<>();
    }

    public frameweb_Vocabulary(
        String vocabularyDocument        ArrayList<frameweb_Axiom> frameweb_axioms,        ArrayList<frameweb_Annotation> frameweb_annotations,        ArrayList<frameweb_IRI> frameweb_iris    ) {
        this.vocabularyDocument = vocabularyDocument;
        this.frameweb_axioms = frameweb_axioms;
        this.frameweb_annotations = frameweb_annotations;
        this.frameweb_iris = frameweb_iris;
    }

    public String getVocabularydocument() {
        return vocabularyDocument;
    }

    public void setVocabularydocument(String vocabularyDocument) {
        this.vocabularyDocument = vocabularyDocument;
    }

    public List<frameweb_Axiom> getFrameweb_axioms() {
        return frameweb_axioms;
    }

    public void addFrameweb_axiom(Frameweb_axiom frameweb_axiom) {
        this.frameweb_axioms.add(frameweb_axiom);
    }
    public frameweb_IRI getFrameweb_iri() {
        return frameweb_iri;
    }

    public void setFrameweb_iri(frameweb_IRI frameweb_iri) {
        this.frameweb_iri = frameweb_iri;
    }
    public List<frameweb_Annotation> getFrameweb_annotations() {
        return frameweb_annotations;
    }

    public void addFrameweb_annotation(Frameweb_annotation frameweb_annotation) {
        this.frameweb_annotations.add(frameweb_annotation);
    }
    public List<frameweb_IRI> getFrameweb_iris() {
        return frameweb_iris;
    }

    public void addFrameweb_iri(Frameweb_iri frameweb_iri) {
        this.frameweb_iris.add(frameweb_iri);
    }

}