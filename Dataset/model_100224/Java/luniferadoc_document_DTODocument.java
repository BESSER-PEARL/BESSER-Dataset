





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_document_DTODocument extends LuniferaDocDocument {

    private String dtoClass;



    public luniferadoc_document_DTODocument(
        String dtoClass    ) {
        super(
        );
        this.dtoClass = dtoClass;
    }


    public String getDtoclass() {
        return dtoClass;
    }

    public void setDtoclass(String dtoClass) {
        this.dtoClass = dtoClass;
    }


}