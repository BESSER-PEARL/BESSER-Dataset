





import java.util.List;
import java.util.ArrayList;

public class spem_Category extends MethodContentElement {






    private spem_DescribableElement spem_describableelement;




    private spem_MethodConfiguration spem_methodconfiguration;




    private spem_MethodConfiguration spem_methodconfiguration;




    private spem_MethodConfiguration spem_methodconfiguration;




    private List<spem_Category> spem_categorys;




    private List<spem_DescribableElement> spem_describableelements;


    public spem_Category(
    ) {
        super(
        );
        this.spem_categorys = new ArrayList<>();
        this.spem_describableelements = new ArrayList<>();
    }

    public spem_Category(
        ArrayList<spem_Category> spem_categorys,        ArrayList<spem_DescribableElement> spem_describableelements    ) {
        this.spem_categorys = spem_categorys;
        this.spem_describableelements = spem_describableelements;
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
    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public spem_MethodConfiguration getSpem_methodconfiguration() {
        return spem_methodconfiguration;
    }

    public void setSpem_methodconfiguration(spem_MethodConfiguration spem_methodconfiguration) {
        this.spem_methodconfiguration = spem_methodconfiguration;
    }
    public List<spem_Category> getSpem_categorys() {
        return spem_categorys;
    }

    public void addSpem_category(Spem_category spem_category) {
        this.spem_categorys.add(spem_category);
    }
    public List<spem_DescribableElement> getSpem_describableelements() {
        return spem_describableelements;
    }

    public void addSpem_describableelement(Spem_describableelement spem_describableelement) {
        this.spem_describableelements.add(spem_describableelement);
    }

}