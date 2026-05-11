





import java.util.List;
import java.util.ArrayList;

public class extended_FormTypes extends AbstractElement {

    private String name;





    private extended_Page extended_page;




    private extended_Entity extended_entity;


    public extended_FormTypes(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public extended_Page getExtended_page() {
        return extended_page;
    }

    public void setExtended_page(extended_Page extended_page) {
        this.extended_page = extended_page;
    }
    public extended_Entity getExtended_entity() {
        return extended_entity;
    }

    public void setExtended_entity(extended_Entity extended_entity) {
        this.extended_entity = extended_entity;
    }

}