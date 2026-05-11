





import java.util.List;
import java.util.ArrayList;

public class dom_FromClass extends JoinEntity, FromRange {

    private boolean popertyFetch;





    private dom_Entity dom_entity;


    public dom_FromClass(
        boolean popertyFetch    ) {
        super(
        );
        this.popertyFetch = popertyFetch;
    }


    public boolean getPopertyfetch() {
        return popertyFetch;
    }

    public void setPopertyfetch(boolean popertyFetch) {
        this.popertyFetch = popertyFetch;
    }

    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }

}