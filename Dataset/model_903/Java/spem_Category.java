





import java.util.List;
import java.util.ArrayList;

public class spem_Category extends MethodContentElement {






    private spem_Category spem_category;




    private spem_MethodConfiguration spem_methodconfiguration;




    private spem_DescribableElement spem_describableelement;




    private spem_MethodConfiguration spem_methodconfiguration;




    private List<spem_DescribableElement> spem_describableelements;




    private spem_MethodConfiguration spem_methodconfiguration;


    public spem_Category(
    ) {
        super(
        );
        this.spem_describableelements = new ArrayList<>();
    }

    public spem_Category(
        ArrayList<spem_DescribableElement> spem_describableelements    ) {
        this.spem_describableelements = spem_describableelements;
    }


    public spem_Category getSpem_category() {
        return spem_category;
    }

    public void setSpem_category(spem_Category spem_category) {
        this.spem_category = spem_category;
    }
    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public spem_DescribableElement getSpem_describableelement() {
        return spem_describableelement;
    }

    public void setSpem_describableelement(spem_DescribableElement spem_describableelement) {
        this.spem_describableelement = spem_describableelement;
    }
    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public List<spem_DescribableElement> getSpem_describableelements() {
        return spem_describableelements;
    }

    public void addSpem_describableelement(Spem_describableelement spem_describableelement) {
        this.spem_describableelements.add(spem_describableelement);
    }
    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }

}