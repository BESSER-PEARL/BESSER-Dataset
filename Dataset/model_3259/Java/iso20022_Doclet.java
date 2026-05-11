





import java.util.List;
import java.util.ArrayList;

public class iso20022_Doclet extends ModelEntity {

    private String content;
    private String type;





    private iso20022_RepositoryConcept iso20022_repositoryconcept;


    public iso20022_Doclet(
        String content,        String type    ) {
        super(
        );
        this.content = content;
        this.type = type;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public iso20022_RepositoryConcept getIso20022_repositoryconcept() {
        return iso20022_repositoryconcept;
    }

    public void setIso20022_repositoryconcept(iso20022_RepositoryConcept iso20022_repositoryconcept) {
        this.iso20022_repositoryconcept = iso20022_repositoryconcept;
    }

}