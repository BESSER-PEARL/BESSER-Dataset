





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_document_EntityDocument extends LuniferaDocDocument {

    private String entityClass;



    public luniferadoc_document_EntityDocument(
        String entityClass    ) {
        super(
        );
        this.entityClass = entityClass;
    }


    public String getEntityclass() {
        return entityClass;
    }

    public void setEntityclass(String entityClass) {
        this.entityClass = entityClass;
    }


}