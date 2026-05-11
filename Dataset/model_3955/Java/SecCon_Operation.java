





import java.util.List;
import java.util.ArrayList;

public class SecCon_Operation extends MultiplicityElement, TypedElement {

    private String body;





    private List<SecCon_Type> seccon_types;


    public SecCon_Operation(
        String body    ) {
        super(
        );
        this.body = body;
        this.seccon_types = new ArrayList<>();
    }

    public SecCon_Operation(
        String body        ArrayList<SecCon_Type> seccon_types    ) {
        this.body = body;
        this.seccon_types = seccon_types;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<SecCon_Type> getSeccon_types() {
        return seccon_types;
    }

    public void addSeccon_type(Seccon_type seccon_type) {
        this.seccon_types.add(seccon_type);
    }

}