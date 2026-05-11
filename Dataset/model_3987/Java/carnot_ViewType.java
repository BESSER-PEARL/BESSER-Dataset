





import java.util.List;
import java.util.ArrayList;

public class carnot_ViewType extends IExtensibleElement, IModelElement {

    private String name;





    private carnot_ViewType carnot_viewtype;


    public carnot_ViewType(
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

    public carnot_ViewType getCarnot_viewtype() {
        return carnot_viewtype;
    }

    public void setCarnot_viewtype(carnot_ViewType carnot_viewtype) {
        this.carnot_viewtype = carnot_viewtype;
    }

}