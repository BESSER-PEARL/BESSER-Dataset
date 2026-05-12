





import java.util.List;
import java.util.ArrayList;

public class pivot_InstanceSpecification extends NamedElement {






    private pivot_Package pivot_package;




    private pivot_Package pivot_package;




    private pivot_LanguageExpression pivot_languageexpression;




    private List<pivot_Class> pivot_classs;




    private List<pivot_Slot> pivot_slots;




    private pivot_Slot pivot_slot;


    public pivot_InstanceSpecification(
    ) {
        super(
        );
        this.pivot_classs = new ArrayList<>();
        this.pivot_slots = new ArrayList<>();
    }

    public pivot_InstanceSpecification(
        ArrayList<pivot_Class> pivot_classs,        ArrayList<pivot_Slot> pivot_slots    ) {
        this.pivot_classs = pivot_classs;
        this.pivot_slots = pivot_slots;
    }


    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public pivot_LanguageExpression getPivot_languageexpression() {
        return pivot_languageexpression;
    }

    public void setPivot_languageexpression(pivot_LanguageExpression pivot_languageexpression) {
        this.pivot_languageexpression = pivot_languageexpression;
    }
    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }
    public List<pivot_Slot> getPivot_slots() {
        return pivot_slots;
    }

    public void addPivot_slot(Pivot_slot pivot_slot) {
        this.pivot_slots.add(pivot_slot);
    }
    public pivot_Slot getPivot_slot() {
        return pivot_slot;
    }

    public void setPivot_slot(pivot_Slot pivot_slot) {
        this.pivot_slot = pivot_slot;
    }

}