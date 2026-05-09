





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_AnnotationCS extends ModelElementCS {

    private String idSource;
    private String stringSource;



    public oclinEcoreCST_AnnotationCS(
        String idSource,        String stringSource    ) {
        super(
        );
        this.idSource = idSource;
        this.stringSource = stringSource;
    }


    public String getIdsource() {
        return idSource;
    }

    public void setIdsource(String idSource) {
        this.idSource = idSource;
    }
    public String getStringsource() {
        return stringSource;
    }

    public void setStringsource(String stringSource) {
        this.stringSource = stringSource;
    }


}