





import java.util.List;
import java.util.ArrayList;

public class Docbook_SurnameType  {

    private String mixed;





    private Docbook_PersonnameType docbook_personnametype;


    public Docbook_SurnameType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_PersonnameType getDocbook_personnametype() {
        return docbook_personnametype;
    }

    public void setDocbook_personnametype(Docbook_PersonnameType docbook_personnametype) {
        this.docbook_personnametype = docbook_personnametype;
    }

}