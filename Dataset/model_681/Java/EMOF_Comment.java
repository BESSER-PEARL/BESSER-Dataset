





import java.util.List;
import java.util.ArrayList;

public class EMOF_Comment extends Element {

    private String body;





    private List<NamedElement> namedelements;


    public EMOF_Comment(
        String body    ) {
        super(
        );
        this.body = body;
        this.namedelements = new ArrayList<>();
    }

    public EMOF_Comment(
        String body        ArrayList<NamedElement> namedelements    ) {
        this.body = body;
        this.namedelements = namedelements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }

}