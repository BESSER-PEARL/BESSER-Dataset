





import java.util.List;
import java.util.ArrayList;

public class publication_Indexing  {

    private String keywords;





    private publication_BiblioReference publication_biblioreference;




    private publication_LegalEntity publication_legalentity;




    private List<publication_SimpleOntologyTerm> publication_simpleontologyterms;




    private publication_BiblioReference publication_biblioreference;




    private List<publication_SimpleOntologyTerm> publication_simpleontologyterms;


    public publication_Indexing(
        String keywords    ) {
        this.keywords = keywords;
        this.publication_simpleontologyterms = new ArrayList<>();
        this.publication_simpleontologyterms = new ArrayList<>();
    }

    public publication_Indexing(
        String keywords        ArrayList<publication_SimpleOntologyTerm> publication_simpleontologyterms,        ArrayList<publication_SimpleOntologyTerm> publication_simpleontologyterms    ) {
        this.keywords = keywords;
        this.publication_simpleontologyterms = publication_simpleontologyterms;
        this.publication_simpleontologyterms = publication_simpleontologyterms;
    }

    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public publication_BiblioReference getPublication_biblioreference() {
        return publication_biblioreference;
    }

    public void setPublication_biblioreference(publication_BiblioReference publication_biblioreference) {
        this.publication_biblioreference = publication_biblioreference;
    }
    public publication_LegalEntity getPublication_legalentity() {
        return publication_legalentity;
    }

    public void setPublication_legalentity(publication_LegalEntity publication_legalentity) {
        this.publication_legalentity = publication_legalentity;
    }
    public List<publication_SimpleOntologyTerm> getPublication_simpleontologyterms() {
        return publication_simpleontologyterms;
    }

    public void addPublication_simpleontologyterm(Publication_simpleontologyterm publication_simpleontologyterm) {
        this.publication_simpleontologyterms.add(publication_simpleontologyterm);
    }
    public publication_BiblioReference getPublication_biblioreference() {
        return publication_biblioreference;
    }

    public void setPublication_biblioreference(publication_BiblioReference publication_biblioreference) {
        this.publication_biblioreference = publication_biblioreference;
    }
    public List<publication_SimpleOntologyTerm> getPublication_simpleontologyterms() {
        return publication_simpleontologyterms;
    }

    public void addPublication_simpleontologyterm(Publication_simpleontologyterm publication_simpleontologyterm) {
        this.publication_simpleontologyterms.add(publication_simpleontologyterm);
    }

}